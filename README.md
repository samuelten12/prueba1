# Aplicación sencilla con Tkinter

Esta aplicación en Python muestra una ventana que pide un texto y, al pulsar el botón (o Enter), muestra ese mismo texto en una ventana emergente.

Requisitos
- Python 3 (Tkinter incluido). En Windows, instala Python desde https://www.python.org/ si no lo tienes.

Ejecutar (PowerShell):

```powershell
cd 'C:\Users\tenjo\newproyect'
python .\app.py
```

Notas
- Si aparece un error relacionado con Tkinter, instala la versión de Python que incluya el soporte para Tcl/Tk.

Empaquetar como .exe (Windows)
 - Recomendado: usa `PyInstaller` para crear un único ejecutable.
 - Desde PowerShell en el directorio del proyecto:

```powershell
cd 'C:\Users\tenjo\newproyect'
python -m pip install --upgrade pip
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --onefile --windowed --name MostrarTexto app.py
```

 - También incluí un script para automatizarlo: `build_exe.ps1`.
	 Ejecuta:

```powershell
cd 'C:\Users\tenjo\newproyect'
.\build_exe.ps1
```

 - El ejecutable resultante estará en `dist\MostrarTexto.exe` (o con el nombre que indiques).

Notas sobre empaquetado
 - Algunos antivirus pueden marcar ejecutables recién creados; esto es un falso positivo frecuente.
 - Si usas dependencias adicionales, puede que necesites ajustar opciones de PyInstaller o incluir archivos extra.
