<#
Simple PowerShell build script to create a single-file Windows executable
using PyInstaller. Run this from PowerShell in the project folder.

Usage:
  .\build_exe.ps1          # builds MostrarTexto.exe
  .\build_exe.ps1 -Name MyApp # builds MyApp.exe
#>

param(
    [string]$Name = "MostrarTexto"
)

Write-Host "Asegurando pip y PyInstaller..."
python -m pip install --upgrade pip
python -m pip install pyinstaller

Write-Host "Construyendo .exe con PyInstaller (onefile, windowed)..."
pyinstaller --noconfirm --onefile --windowed --name $Name app.py

Write-Host "Listo. Busca el ejecutable en la carpeta 'dist' (archivo: $Name.exe)"
