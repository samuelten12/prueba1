# Script para compilar la aplicación en ejecutable
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Compilando aplicación..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Cambiar a directorio del proyecto
Set-Location "c:\Users\tenjo\newproyect"

# Ejecutar PyInstaller
Write-Host "Generando ejecutable..." -ForegroundColor Yellow
pyinstaller --onefile `
    --windowed `
    --name="BalanceadorEcuaciones" `
    --distpath="./dist" `
    --workpath="./build" `
    --specpath="." `
    app_gui.py

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "¡Compilación completada!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "El ejecutable se encuentra en:" -ForegroundColor Yellow
Write-Host "  c:\Users\tenjo\newproyect\dist\BalanceadorEcuaciones.exe" -ForegroundColor Green
Write-Host ""
