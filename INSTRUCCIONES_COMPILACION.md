# Instrucciones de Compilación con PyInstaller

## 1. Requisitos Previos

Antes de compilar, asegúrate de tener instalados:

```powershell
# Instalar Python (si no lo tienes)
# Descargar desde: https://www.python.org/downloads/

# Verificar que Python está instalado
python --version

# Instalar PyInstaller
pip install pyinstaller
```

## 2. Método Simple (Recomendado)

### Paso 1: Abrir PowerShell
Navega a la carpeta del proyecto:
```powershell
cd C:\Users\tenjo\newproyect
```

### Paso 2: Ejecutar PyInstaller
Para crear un ejecutable de una sola línea (una sola carpeta sin dependencias externas):

```powershell
pyinstaller --onefile --windowed --name="BalanceadorEcuaciones" app_gui.py
```

### Paso 3: Encontrar el Ejecutable
El .exe se creará en la carpeta `dist/`:
```powershell
C:\Users\tenjo\newproyect\dist\BalanceadorEcuaciones.exe
```

---

## 3. Método Avanzado (Con Carpeta de Salida Limpia)

Si quieres organizar mejor los archivos:

```powershell
pyinstaller `
  --onefile `
  --windowed `
  --name="BalanceadorEcuaciones" `
  --distpath="./dist" `
  --workpath="./build" `
  --specpath="." `
  app_gui.py
```

**Explicación de opciones:**
- `--onefile` → Crea un único .exe (sin dependencias en carpeta)
- `--windowed` → Oculta la consola (interfaz gráfica limpia)
- `--name="BalanceadorEcuaciones"` → Nombre del ejecutable
- `--distpath="./dist"` → Carpeta de salida
- `--workpath="./build"` → Carpeta de trabajo temporal
- `--specpath="."` → Dónde guardar el archivo .spec

---

## 4. Método con Script PowerShell

Crea un archivo llamado `compilar.ps1`:

```powershell
# Script para compilar automáticamente
Write-Host "Compilando Balanceador de Ecuaciones..." -ForegroundColor Cyan

pyinstaller --onefile --windowed --name="BalanceadorEcuaciones" app_gui.py

Write-Host ""
Write-Host "Compilacion completada!" -ForegroundColor Green
Write-Host "Ejecutable: ./dist/BalanceadorEcuaciones.exe" -ForegroundColor Yellow
```

Luego ejecuta:
```powershell
powershell -ExecutionPolicy Bypass -File .\compilar.ps1
```

---

## 5. Opciones Útiles de PyInstaller

### Agregar un icono personalizado
```powershell
pyinstaller --onefile --windowed --icon="ruta/al/icono.ico" app_gui.py
```

### Incluir archivos adicionales
```powershell
pyinstaller --onefile --windowed --add-data "datos/:datos/" app_gui.py
```

### Reducir tamaño del ejecutable
```powershell
pyinstaller --onefile --windowed -y --optimize=2 app_gui.py
```

### Ver todos los parámetros disponibles
```powershell
pyinstaller --help
```

---

## 6. Solución de Problemas

### Error: "pyinstaller no se reconoce"
**Solución:** Instala PyInstaller nuevamente:
```powershell
pip install --upgrade pyinstaller
```

### Error: "No module named 'tkinter'"
**Solución:** Tkinter debería venir con Python. Si no:
```powershell
# En Windows, reinstala Python marcando "tcl/tk and IDLE" en la instalación
```

### Antivirus bloquea el ejecutable
**Solución:** Es normal. El usuario puede:
1. Descargar nuevamente
2. Marcar como "aplicación segura" en el antivirus
3. Ejecutar como administrador

### El ejecutable es muy grande (~100 MB)
**Es normal.** PyInstaller incluye todo el entorno de Python. Para reducir:
```powershell
pyinstaller --onefile --windowed -y --exclude-module=numpy app_gui.py
```

---

## 7. Distribuir el Ejecutable

Una vez compilado, tienes tres opciones:

### Opción A: Solo el .exe
```powershell
# Copia solo el archivo dist/BalanceadorEcuaciones.exe
# Usuarios lo ejecutan directamente
```

### Opción B: Carpeta completa
```powershell
# Copia toda la carpeta dist/
# Usuarios ejecutan el .exe dentro
```

### Opción C: Empaquetado como ZIP
```powershell
Compress-Archive -Path .\dist\BalanceadorEcuaciones.exe -DestinationPath .\BalanceadorEcuaciones.zip
```

---

## 8. Automatizar la Compilación Completa

Crear archivo `build_completo.ps1`:

```powershell
# Limpiar compilaciones anteriores
Remove-Item -Path "./dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "./build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.spec" -Force -ErrorAction SilentlyContinue

# Compilar
Write-Host "Compilando..." -ForegroundColor Cyan
pyinstaller --onefile --windowed --name="BalanceadorEcuaciones" app_gui.py

# Crear paquete ZIP
Write-Host "Empaquetando..." -ForegroundColor Yellow
Compress-Archive -Path "./dist/BalanceadorEcuaciones.exe" `
                -DestinationPath "./BalanceadorEcuaciones_v1.0.zip" `
                -Force

Write-Host "Completado!" -ForegroundColor Green
Write-Host "Archivo ZIP: ./BalanceadorEcuaciones_v1.0.zip" -ForegroundColor Yellow
```

Ejecutar:
```powershell
powershell -ExecutionPolicy Bypass -File .\build_completo.ps1
```

---

## 9. Verificar que el Ejecutable Funciona

```powershell
# Ejecutar directamente
.\dist\BalanceadorEcuaciones.exe

# O cambiar a la carpeta
cd dist
.\BalanceadorEcuaciones.exe
```

---

## Resumen Rápido

| Necesidad | Comando |
|-----------|---------|
| Compilación simple | `pyinstaller --onefile --windowed app_gui.py` |
| Con carpetas limpias | `pyinstaller --onefile --windowed --distpath="./dist" --workpath="./build" app_gui.py` |
| Con icono | `pyinstaller --onefile --windowed --icon="icono.ico" app_gui.py` |
| Reducir tamaño | `pyinstaller --onefile --windowed -y --optimize=2 app_gui.py` |

---

¡Listo! Ya puedes compilar tu aplicación en cualquier momento.
