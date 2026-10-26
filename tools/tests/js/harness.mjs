// Loads the shipped deploy/background.js into a vm sandbox with an in-memory
// chrome.* mock so background logic can be exercised without a browser.
// Never opens windows, tabs or processes: chrome.tabs/windows are recording stubs.
import fs from 'node:fs'
import path from 'node:path'
import vm from 'node:vm'
import { fileURLToPath } from 'node:url'
import { webcrypto } from 'node:crypto'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..')

function event() {
    const listeners = []
    return { addListener: fn => listeners.push(fn), listeners, fire: (...a) => Promise.all(listeners.map(fn => fn(...a))) }
}

// tree: { id, title, children? | url? } ; root id is '0'
export function createBookmarkStore(rootNode) {
    const nodes = new Map()
    function index(node, parentId) {
        node.parentId = parentId
        nodes.set(node.id, node)
        if (node.children) node.children.forEach((c, i) => { c.index = i; index(c, node.id) })
    }
    index(rootNode, undefined)
    const clean = n => {
        const o = { ...n }
        delete o.children
        return o
    }
    const full = n => {
        const o = { ...n }
        if (n.children) o.children = n.children.map(full)
        return o
    }
    const reindex = p => p.children.forEach((c, i) => { c.index = i })
    return {
        nodes,
        moves: [],
        get: async id => {
            if (!nodes.has(id)) throw new Error('Can\'t find bookmark for id.')
            return [clean(nodes.get(id))]
        },
        getChildren: async id => {
            if (!nodes.has(id)) throw new Error('Can\'t find bookmark for id.')
            return (nodes.get(id).children || []).map(clean)
        },
        getTree: async () => [full(rootNode)],
        move: async function (id, dest) {
            const n = nodes.get(id)
            const from = nodes.get(n.parentId)
            from.children.splice(n.index, 1)
            reindex(from)
            const to = nodes.get(dest.parentId)
            const i = dest.index === undefined ? to.children.length : dest.index
            to.children.splice(i, 0, n)
            n.parentId = to.id
            reindex(to)
            this.moves.push([id, dest.parentId, dest.index])
            return clean(n)
        },
        remove: async id => {
            const n = nodes.get(id)
            if (!n) throw new Error('Can\'t find bookmark for id.')
            if (n.children && n.children.length) throw new Error('Can\'t remove non-empty folder')
            const p = nodes.get(n.parentId)
            p.children.splice(n.index, 1)
            reindex(p)
            nodes.delete(id)
        },
        titlesOf: id => nodes.get(id).children.map(c => c.title)
    }
}

export async function load({ tree, storage = {}, userAgent = 'Mozilla/5.0 Chrome/130.0 Safari/537.36', overrides = {} } = {}) {
    const store = createBookmarkStore(tree)
    const mem = { ...storage }
    const ev = {
        action: { onClicked: event() },
        bookmarks: {
            onChanged: event(), onChildrenReordered: event(), onCreated: event(),
            onImportBegan: event(), onImportEnded: event(), onMoved: event(), onRemoved: event()
        },
        runtime: { onConnect: event() }
    }
    const calls = { tabsCreate: [], tabsUpdate: [], windowsUpdate: [] }
    const chrome = {
        action: {
            ...ev.action,
            setBadgeBackgroundColor: async () => {}, setBadgeText: async () => {},
            setIcon: (d, cb) => cb && cb()
        },
        bookmarks: {
            ...ev.bookmarks,
            get: id => store.get(id), getChildren: id => store.getChildren(id), getTree: () => store.getTree(),
            move: (id, d) => store.move(id, d), remove: id => store.remove(id)
        },
        runtime: {
            ...ev.runtime, lastError: undefined,
            connect: () => { throw new Error('connect not mocked') },
            getManifest: () => ({ version: '2026.8.28.0' }),
            getURL: p => 'chrome-extension://test' + p
        },
        storage: {
            local: {
                get: (k, cb) => cb(typeof k === 'string' ? (k in mem ? { [k]: mem[k] } : {}) : { ...mem }),
                set: (o, cb) => { Object.assign(mem, JSON.parse(JSON.stringify(o))); cb() },
                remove: (k, cb) => { delete mem[k]; cb() }
            }
        },
        tabs: { create: async o => { calls.tabsCreate.push(o) }, update: async (...a) => { calls.tabsUpdate.push(a) } },
        windows: { update: async (...a) => { calls.windowsUpdate.push(a) } }
    }
    const selfObj = { addEventListener() {}, skipWaiting: async () => {} }
    const sandbox = {
        chrome, self: selfObj, navigator: { userAgent }, crypto: webcrypto, TextEncoder, URL,
        console, setTimeout, clearTimeout, setInterval, clearInterval, Date, Intl, ...overrides
    }
    vm.createContext(sandbox)
    let code = fs.readFileSync(path.join(root, 'deploy', 'background.js'), 'utf8')
    // expose top-level consts of the service worker script to the test
    code += '\n;this.__t = { local, shared, bookmark_resort, bookmark_sort, bookmark_compare, start, start_done, listener_port_message,' +
        ' listener_bookmark_import_began, listener_bookmark_import_ended, tool_bookmark_history_log, bookmark_get_location,' +
        ' tool_empty_folders_remove, tool_duplicate_bookmarks_remove, tool_similar_bookmarks_remove, bookmark_get_hashes, version_less_than,' +
        ' refresh_about, refresh_tools, human_time_since }\n'
    vm.runInContext(code, sandbox, { filename: 'deploy/background.js' })
    const t = sandbox.__t
    await t.start_done()
    return { t, store, chrome, ev, mem, calls, sandbox }
}
