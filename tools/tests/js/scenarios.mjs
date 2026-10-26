// Usage: node scenarios.mjs <name>  -> prints one JSON result line. No windows/processes are started.
import { load } from './harness.mjs'

const AUTO = { option_automatic_sorting: true, option_group_folders: true, option_bookmarks_bar: true,
    option_bookmarks_bar_sort: 'alpha', version: '2026.8.28.0' }
const bar = children => ({ id: '0', title: '', children: [{ id: '1', title: 'Bookmarks bar', children }] })

const scenarios = {
    // sorted order is the original-index permutation whose concatenated indexes equal the identity string
    async collision() {
        const S = [0, 12, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 2]
        const title = []
        S.forEach((idx, pos) => { title[idx] = 't' + String(pos).padStart(2, '0') })
        const r = await load({ tree: bar(title.map((t, i) => ({ id: '1' + i, title: t, url: 'https://x/' + t }))), storage: AUTO })
        return { titles: r.store.titlesOf('1') }
    }
}

const out = await scenarios[process.argv[2]]()
console.log(JSON.stringify(out))
process.exit(0)
