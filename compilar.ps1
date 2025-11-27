# Script automatizado para compilar con PyInstaller
# Uso: powershell -ExecutionPolicy Bypass -File .\compilar.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Compilador - Balanceador de Ecuaciones" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si PyInstaller está instalado
$pyinstaller = Get-Command pyinstaller -ErrorAction SilentlyContinue

if (-not $pyinstaller) {
    Write-Host "PyInstaller no está instalado." -ForegroundColor Red
    Write-Host "Instalando PyInstaller..." -ForegroundColor Yellow
    pip install pyinstaller
    Write-Host ""
}

# Limpiar compilaciones anteriores
Write-Host "Limpiando compilaciones anteriores..." -ForegroundColor Yellow
Remove-Item -Path "./dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "./build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.spec" -Force -ErrorAction SilentlyContinue

# Compilar
Write-Host "Compilando aplicacion..." -ForegroundColor Cyan
pyinstaller --onefile --windowed --name="BalanceadorEcuaciones" app_gui.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Compilacion exitosa!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Ejecutable creado en:" -ForegroundColor Yellow
    Write-Host "  $((Get-Location).Path)\dist\BalanceadorEcuaciones.exe" -ForegroundColor Green
    Write-Host ""
    Write-Host "Puedes ejecutarlo con:" -ForegroundColor Yellow
    Write-Host "  .\dist\BalanceadorEcuaciones.exe" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Error en la compilacion. Verifica los mensajes arriba." -ForegroundColor Red
    Write-Host ""
}
