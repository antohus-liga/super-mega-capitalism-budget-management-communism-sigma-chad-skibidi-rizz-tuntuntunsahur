New-Item -ItemType Directory -Force -Path builds/windows | Out-Null

uv run pyinstaller pyinstaller.spec

$exePath = "builds/windows/familybudget/familybudget.exe"
$targetPath = "builds/windows/familybudget.exe"

if (Test-Path $exePath) {
    Copy-Item $exePath $targetPath -Force
}

Remove-Item -Recurse -Force build -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue

Write-Host "Windows build complete → builds/windows/familybudget.exe"