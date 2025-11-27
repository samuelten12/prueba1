# Script para crear un paquete distribuible
Write-Host "Creando paquete..." -ForegroundColor Cyan

$outputFolder = "BalanceadorEcuaciones_v1.0"
$sourceFolder = "dist"

if (Test-Path $outputFolder) {
    Remove-Item $outputFolder -Recurse -Force
}
New-Item -ItemType Directory -Path $outputFolder | Out-Null

Copy-Item "$sourceFolder\BalanceadorEcuaciones.exe" -Destination "$outputFolder\" -Force
Write-Host "OK: Ejecutable copiado" -ForegroundColor Green

Copy-Item "README.md" -Destination "$outputFolder\LEEME.txt" -Force
Write-Host "OK: Instrucciones copiadas" -ForegroundColor Green

Write-Host ""
Write-Host "Empaquetado completado en: $outputFolder" -ForegroundColor Green
