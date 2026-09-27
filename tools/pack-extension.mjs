#!/usr/bin/env node
/**
 * 打包 Chrome Web Store 上架 zip 與目錄。
 * 用法：node tools/pack-extension.mjs
 */
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const manifestPath = path.join(root, 'deploy', 'manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const version = manifest.version || '0.0.0';
const name = 'sprucemarks';

const distDir = path.join(root, 'dist');
const outDir = path.join(distDir, `${name}-${version}`);
const zipPath = path.join(distDir, `${name}-${version}.zip`);
const shaPath = path.join(distDir, `${name}-${version}.zip.sha256`);

console.log(`==> 打包 Sprucemarks v${version}...`);

// 優先嘗試 pwsh，若在 Windows 且找不到 pwsh 則 fallback 至 powershell
const ps1Script = path.join(root, 'tools', 'pack_extension.ps1');
const candidates = process.platform === 'win32' ? ['pwsh', 'powershell'] : ['pwsh'];

let packRun = null;
for (const cmd of candidates) {
  packRun = spawnSync(cmd, ['-NoProfile', '-File', ps1Script], {
    cwd: root,
    stdio: 'inherit',
  });
  if (packRun.error && packRun.error.code === 'ENOENT') {
    continue;
  }
  break;
}

if (!packRun || packRun.status !== 0) {
  if (packRun && packRun.error) {
    console.error('打包執行失敗:', packRun.error.message);
  }
  process.exit((packRun && packRun.status) || 1);
}
