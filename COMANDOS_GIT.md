# Comandos Git para Actualizar Repositorio Existente

## 1. Configuración Inicial (Una sola vez)

```powershell
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email
git config --global user.email "tu_email@github.com"

# Verificar la configuración
git config --global --list
```

---

## 2. Clonar un Repositorio Existente

Si el repositorio ya existe en GitHub y quieres descargarlo:

```powershell
# Clonar repositorio con HTTPS
git clone https://github.com/samuelten12/prueba1.git

# O con SSH (si tienes clave SSH)
git clone git@github.com:samuelten12/prueba1.git

# Cambiar a la carpeta
cd prueba1
```

---

## 3. Ver el Estado del Repositorio

```powershell
# Ver cambios sin confirmar
git status

# Ver cambios en detalle
git diff

# Ver historial de commits
git log

# Ver últimos 5 commits
git log -5

# Ver rama actual
git branch
```

---

## 4. Actualizar Cambios Locales

### Opción A: Agregar todos los cambios

```powershell
# Agregar todos los archivos modificados
git add .

# Ver cambios preparados
git status
```

### Opción B: Agregar archivos específicos

```powershell
# Agregar un archivo
git add archivo.py

# Agregar varios archivos
git add archivo1.py archivo2.md

# Agregar todos los archivos de una carpeta
git add carpeta/
```

---

## 5. Confirmar Cambios (Crear Commit)

```powershell
# Commit simple
git commit -m "Descripcion del cambio"

# Commit con descripción larga
git commit -m "Titulo del cambio" -m "Descripcion detallada aqui"

# Ejemplos de mensajes buenos:
git commit -m "Agrega balanceador de ecuaciones"
git commit -m "Corrige bug en interfaz grafica"
git commit -m "Actualiza documentacion"
git commit -m "Mejora rendimiento del algoritmo"
```

---

## 6. Subir Cambios a GitHub (Push)

```powershell
# Subir a la rama principal (primera vez)
git push -u origin main

# Subir a rama principal (siguientes veces)
git push

# Subir a rama específica
git push origin nombre-rama

# Forzar push (usar con cuidado)
git push --force
```

---

## 7. Descargar Cambios de GitHub (Pull)

```powershell
# Descargar cambios de GitHub
git pull

# Descargar cambios de rama específica
git pull origin main

# Ver cambios antes de fusionar
git fetch
git diff origin/main
```

---

## 8. Flujo Completo de Actualización

### Paso 1: Verificar estado
```powershell
cd c:\Users\tenjo\newproyect
git status
```

### Paso 2: Agregar cambios
```powershell
git add .
```

### Paso 3: Confirmar
```powershell
git commit -m "Descripcion del cambio"
```

### Paso 4: Subir a GitHub
```powershell
git push
```

---

## 9. Casos Comunes

### Actualizar después de hacer cambios

```powershell
# En una sola línea (recomendado)
git add . ; git commit -m "Actualización" ; git push

# O paso a paso
git add .
git commit -m "Actualización"
git push
```

### Ver qué cambios se subirán

```powershell
# Ver cambios antes de hacer commit
git diff

# Ver cambios antes de hacer push
git log origin/main..HEAD
```

### Deshacer cambios locales

```powershell
# Deshacer cambios en un archivo
git checkout archivo.py

# Deshacer todos los cambios locales
git reset --hard

# Deshacer el último commit (mantener cambios)
git reset --soft HEAD~1

# Deshacer el último commit (perder cambios)
git reset --hard HEAD~1
```

### Crear rama nueva

```powershell
# Crear rama
git checkout -b nombre-rama

# Cambiar a rama existente
git checkout main

# Listar ramas
git branch -a

# Subir rama nueva a GitHub
git push -u origin nombre-rama
```

---

## 10. Solución de Problemas

### Error: "Your branch is ahead"

```powershell
# Los cambios están listos para subir
git push
```

### Error: "Your branch is behind"

```powershell
# Descargar cambios del servidor
git pull

# Si hay conflictos, resuelve manualmente y luego:
git add .
git commit -m "Merge cambios"
git push
```

### Error: "fatal: not a git repository"

```powershell
# No estás en un repositorio Git
# Inicializa uno nuevo:
git init

# O clona un repositorio existente:
git clone https://github.com/usuario/repo.git
```

### Conflictos de fusión

```powershell
# Ver conflictos
git status

# Editar archivos conflictivos manualmente

# Después de resolver:
git add .
git commit -m "Resuelve conflictos"
git push
```

---

## 11. Comandos Útiles Rápida Referencia

| Comando | Descripción |
|---------|-------------|
| `git status` | Ver estado actual |
| `git add .` | Agregar todos los cambios |
| `git commit -m "msg"` | Crear commit |
| `git push` | Subir a GitHub |
| `git pull` | Descargar cambios |
| `git log` | Ver historial |
| `git diff` | Ver diferencias |
| `git branch` | Ver ramas |
| `git checkout -b rama` | Crear rama nueva |
| `git merge rama` | Fusionar rama |
| `git reset --hard` | Deshacer cambios |
| `git clone URL` | Clonar repositorio |

---

## 12. Tu Repositorio Actual

**Información:**
- URL: https://github.com/samuelten12/prueba1.git
- Usuario: samuelten12
- Rama: main
- Tipo: Público

**Comandos para tu repositorio:**

```powershell
# Clonar (si aún no lo has hecho)
git clone https://github.com/samuelten12/prueba1.git
cd prueba1

# Actualizar cambios
git add .
git commit -m "Actualiza balanceador de ecuaciones"
git push
```

---

## 13. Workflow Recomendado Diario

```powershell
# 1. Inicio del día: descargar cambios
git pull

# 2. Durante el día: hacer cambios

# 3. Antes de terminar: subir cambios
git add .
git commit -m "Descripcion"
git push

# 4. Ver cambios subidos
git log --oneline -5
```

---

## 14. Crear un `.gitignore`

Para excluir archivos de Git:

```powershell
# Crear archivo .gitignore
New-Item -Path ".gitignore" -Type File

# Agregar contenido (abre con editor y agrega):
```

**Contenido recomendado:**
```
# Carpetas de compilación
build/
dist/
*.spec

# Python
__pycache__/
*.pyc
*.pyo

# Entorno
venv/
env/

# IDE
.vscode/
.idea/

# Sistema
.DS_Store
Thumbs.db
```

---

## Resumen Rápido para Tu Proyecto

```powershell
# 1. Navegar al proyecto
cd c:\Users\tenjo\newproyect

# 2. Ver cambios
git status

# 3. Agregar cambios
git add .

# 4. Crear commit
git commit -m "Actualiza aplicación"

# 5. Subir a GitHub
git push

# Listo! Cambios en GitHub
```

---

**Recuerda:** Haz commits frecuentes con mensajes descriptivos. Sube regularmente tus cambios a GitHub.
