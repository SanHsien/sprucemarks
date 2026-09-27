[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

Write-Host "==> Check Environment"
python -c "import sys; print(f'Python: {sys.version}')"
$nodeCmd = Get-Command node -ErrorAction SilentlyContinue
if ($null -ne $nodeCmd) {
    Write-Host "Node.js: $(& $nodeCmd.Source --version)"
}

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Host "==> Create .venv"
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        throw "python -m venv .venv failed with exit code $LASTEXITCODE"
    }
}

Write-Host "==> Install maintenance dependencies"
& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    throw "pip upgrade failed with exit code $LASTEXITCODE"
}
& $venvPython -m pip install -r (Join-Path $repoRoot "requirements-dev.txt")
if ($LASTEXITCODE -ne 0) {
    throw "pip install requirements-dev.txt failed with exit code $LASTEXITCODE"
}

$psCmd = if (Get-Command pwsh -ErrorAction SilentlyContinue) { "pwsh" } else { "powershell" }

Write-Host "==> Canonical Windows gate"
& $psCmd -NoProfile -File (Join-Path $repoRoot "tools\dev_check.ps1")
if ($LASTEXITCODE -ne 0) {
    throw "tools\dev_check.ps1 failed with exit code $LASTEXITCODE"
}

Write-Host "==> Product extension gate"
& $psCmd -NoProfile -File (Join-Path $repoRoot "tools\test_product.ps1")
if ($LASTEXITCODE -ne 0) {
    throw "tools\test_product.ps1 failed with exit code $LASTEXITCODE"
}

Write-Host ""
Write-Host "維護環境可用。載入擴充功能請參考 README.md 與 docs\DEVELOPMENT.md"
