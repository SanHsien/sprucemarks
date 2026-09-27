[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

$manifestPath = Join-Path $repoRoot "deploy\manifest.json"
if (-not (Test-Path -LiteralPath $manifestPath)) {
    throw "Missing manifest: deploy\manifest.json"
}
$manifest = ConvertFrom-Json (Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8)
$version = $manifest.version
$name = "sprucemarks"

Write-Host "==> Run product validation before packaging"
$psCmd = if (Get-Command pwsh -ErrorAction SilentlyContinue) { "pwsh" } else { "powershell" }
& $psCmd -NoProfile -File (Join-Path $repoRoot "tools\test_product.ps1")
if ($LASTEXITCODE -ne 0) {
    throw "Product validation failed; aborting package"
}

$distDir = Join-Path $repoRoot "dist"
$targetDir = Join-Path $distDir "$name-$version"
$zipPath = Join-Path $distDir "$name-$version.zip"
$shaPath = Join-Path $distDir "$name-$version.zip.sha256"

if (Test-Path -LiteralPath $distDir) {
    Remove-Item -LiteralPath $distDir -Recurse -Force
}
New-Item -ItemType Directory -Path $targetDir -Force | Out-Null

Write-Host "==> Copy deploy files to packaging directory"
$deployDir = Join-Path $repoRoot "deploy"
Copy-Item -Path (Join-Path $deployDir "*") -Destination $targetDir -Recurse -Force

Write-Host "==> Create Chrome Web Store upload zip: $zipPath"
# Compress contents of targetDir so manifest.json is at the root of the zip
$compressItems = Get-ChildItem -Path $targetDir
Compress-Archive -Path $compressItems.FullName -DestinationPath $zipPath -Force

$hash = (Get-FileHash -Path $zipPath -Algorithm SHA256).Hash
Set-Content -Path $shaPath -Value "$hash  $name-$version.zip" -Encoding UTF8

$zipSize = (Get-Item -LiteralPath $zipPath).Length
Write-Host ""
Write-Host "=================================================="
Write-Host "Chrome Web Store 上架包打包完成："
Write-Host "  Zip 檔案： $zipPath ($([math]::Round($zipSize / 1KB, 1)) KB)"
Write-Host "  SHA256：  $hash"
Write-Host "  校驗檔：  $shaPath"
Write-Host "=================================================="
