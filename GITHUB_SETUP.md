# Guía Completa: Subir tu Aplicación a GitHub

## 1. Requisitos Previos

Asegúrate de tener instalados:
```powershell
# Verificar que Git está instalado
git --version

# Si no lo tienes, descárgalo desde: https://git-scm.com/download/win
```

---

## 2. Configurar Git (Primera Vez)

Si es la primera vez que usas Git, configura tu identidad:

```powershell
# Configura tu nombre (global para todos tus proyectos)
git config --global user.name "Tu Nombre"

# Configura tu email (debe ser el mismo de GitHub)
git config --global user.email "tu_email@ejemplo.com"

# Verificar que está configurado
git config --global user.name
git config --global user.email
```

---

## 3. Inicializar Git en tu Proyecto Local

Navega a la carpeta del proyecto:

```powershell
cd C:\Users\tenjo\newproyect
```

Inicializar un repositorio Git:

```powershell
git init
```

---

## 4. Agregar Archivos al Repositorio

Agregar TODOS los archivos:
```powershell
git add .
```

O agregar archivos específicos:
```powershell
git add app_gui.py
git add balanceador_ecuaciones.py
git add README.md
git add INSTRUCCIONES_COMPILACION.md
```

Ver qué archivos serán subidos:
```powershell
git status
```

---

## 5. Crear un .gitignore (Opcional pero Recomendado)

Crear archivo `.gitignore` para excluir carpetas no necesarias:

```powershell
# Crear el archivo
New-Item -Path ".gitignore" -Type File

# Agregar contenido (abre con editor y agrega):
```

Contenido recomendado para `.gitignore`:
```
# Carpetas de compilación
build/
dist/
*.spec

# Caché de Python
__pycache__/
*.pyc
*.pyo
*.egg-info/

# Archivos de entorno
venv/
env/

# IDE
.vscode/
.idea/
*.swp

# Archivos del sistema
.DS_Store
Thumbs.db
```

---

## 6. Hacer el Primer Commit

Confirmar los cambios localmente:

```powershell
git commit -m "Commit inicial: Balanceador de ecuaciones químicas"
```

Cambiar nombre de rama a "main" (si lo necesitas):
```powershell
git branch -M main
```

Ver el historial de commits:
```powershell
git log
```

---

## 7. Crear un Repositorio en GitHub

1. **Ir a GitHub:** https://github.com/login
2. **Crear nuevo repositorio:**
   - Click en "+" → "New repository"
   - Nombre: `balanceador-ecuaciones`
   - Descripción: "Aplicación para balancear ecuaciones químicas con H, C, O, N"
   - Selecciona "Public" o "Private"
   - NO inicialices con README (ya tienes uno)
   - Click en "Create repository"

3. **GitHub te mostrará los comandos.** Usa estos:

---

## 8. Conectar tu Repositorio Local con GitHub

Agregar el repositorio remoto (reemplaza USERNAME y REPO):

```powershell
# Opción A: Con HTTPS (recomendado para principiantes)
git remote add origin https://github.com/samuelten12/balanceador-ecuaciones.git

# Opción B: Con SSH (si tienes clave SSH configurada)
git remote add origin git@github.com:samuelten12/balanceador-ecuaciones.git
```

Verificar que está conectado:
```powershell
git remote -v
```

---

## 9. Subir tu Código a GitHub

Empujar los cambios al servidor remoto:

```powershell
# Primera vez (configura la rama por defecto)
git push -u origin main

# Siguientes veces (más simple)
git push
```

Si pide autenticación:
- **Con HTTPS:** Ingresa tu usuario y contraseña (o token personal)
- **Con SSH:** Debería funcionar automáticamente si tienes clave SSH

---

## 10. Verificar que Fue Subido

Abre tu navegador y ve a:
```
https://github.com/samuelten12/balanceador-ecuaciones
```

Deberías ver todos tus archivos allá.

---

## 11. Comandos para Cambios Futuros

Cada vez que hagas cambios:

```powershell
# Ver cambios
git status

# Agregar cambios
git add .

# Confirmar cambios
git commit -m "Descripción del cambio"

# Subir a GitHub
git push
```

---

## 12. Flujo Completo (Resumen Rápido)

```powershell
# 1. Configuración inicial (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@ejemplo.com"

# 2. Inicializar repositorio
cd C:\Users\tenjo\newproyect
git init

# 3. Crear .gitignore
New-Item -Path ".gitignore" -Type File
# (Edita el archivo con tu editor)

# 4. Agregar archivos
git add .

# 5. Primer commit
git commit -m "Commit inicial: Balanceador de ecuaciones químicas"

# 6. Configurar rama
git branch -M main

# 7. Conectar a GitHub (reemplaza USERNAME y REPO)
git remote add origin https://github.com/samuelten12/balanceador-ecuaciones.git

# 8. Subir a GitHub
git push -u origin main
```

---

## 13. Solución de Problemas

### Error: "fatal: not a git repository"
**Solución:** Ejecuta `git init` en la carpeta correcta:
```powershell
cd C:\Users\tenjo\newproyect
git init
```

### Error: "fatal: could not read Username"
**Solución 1 (HTTPS):** Ingresa tu token personal:
1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Genera un nuevo token
3. Cópialo y úsalo como contraseña

**Solución 2 (SSH):** Configura clave SSH:
```powershell
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"

# Ver clave pública
cat $env:USERPROFILE\.ssh\id_ed25519.pub

# Copiar la clave y agregarla en GitHub → Settings → SSH keys
```

### Error: "updates were rejected because the tip of your current branch is behind"
```powershell
# Traer cambios del servidor
git pull origin main

# Luego intenta subir de nuevo
git push origin main
```

### Eliminar un archivo que ya está en GitHub
```powershell
git rm --cached archivo.txt
git commit -m "Remove archivo.txt"
git push
```

---

## 14. Estructura Recomendada en GitHub

Tu repositorio debería verse así:
```
balanceador-ecuaciones/
├── app_gui.py
├── balanceador_ecuaciones.py
├── compilar.ps1
├── README.md
├── INSTRUCCIONES_COMPILACION.md
├── DISTRIBUCION.txt
├── .gitignore
└── dist/
    └── BalanceadorEcuaciones.exe
```

---

## 15. Comandos Git Más Útiles

| Comando | Descripción |
|---------|-------------|
| `git status` | Ver cambios sin confirmar |
| `git add .` | Agregar todos los cambios |
| `git commit -m "mensaje"` | Confirmar cambios |
| `git push` | Subir a GitHub |
| `git pull` | Descargar cambios de GitHub |
| `git log` | Ver historial de commits |
| `git branch` | Ver ramas disponibles |
| `git checkout -b nueva-rama` | Crear nueva rama |
| `git diff` | Ver diferencias en los archivos |
| `git reset --hard` | Deshacer todos los cambios locales |

---

## 16. Tu Repositorio Actual

Tu repositorio ya existe en GitHub:
```
Repository: prueba1
Owner: samuelten12
URL: https://github.com/samuelten12/prueba1
```

Si quieres subir el Balanceador allí, usa:
```powershell
git remote add origin https://github.com/samuelten12/prueba1.git
git push -u origin main
```

O crea un repositorio nuevo específicamente para la aplicación.

---

¡Listo! Ahora tienes todo lo necesario para subir tu aplicación a GitHub.
