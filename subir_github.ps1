# Script automatizado para subir a GitHub
# Uso: powershell -ExecutionPolicy Bypass -File .\subir_github.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Subidor de Código a GitHub" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Git está instalado
$git = Get-Command git -ErrorAction SilentlyContinue

if (-not $git) {
    Write-Host "Git no está instalado." -ForegroundColor Red
    Write-Host "Descargalo desde: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit
}

# Verificar si ya hay un repositorio Git
if (-not (Test-Path ".git")) {
    Write-Host "Inicializando repositorio Git..." -ForegroundColor Yellow
    git init
    Write-Host "OK: Repositorio inicializado" -ForegroundColor Green
    Write-Host ""
}

# Configurar usuario (opcional)
$userName = git config --global user.name
$userEmail = git config --global user.email

if (-not $userName -or -not $userEmail) {
    Write-Host "Configurando usuario de Git..." -ForegroundColor Yellow
    $nombre = Read-Host "Ingresa tu nombre"
    $email = Read-Host "Ingresa tu email de GitHub"
    git config --global user.name "$nombre"
    git config --global user.email "$email"
    Write-Host "OK: Usuario configurado" -ForegroundColor Green
    Write-Host ""
}

# Ver estado
Write-Host "Estado actual:" -ForegroundColor Yellow
git status
Write-Host ""

# Agregar archivos
Write-Host "Agregando archivos..." -ForegroundColor Cyan
git add .
Write-Host "OK: Archivos agregados" -ForegroundColor Green
Write-Host ""

# Crear commit
Write-Host "Creando commit..." -ForegroundColor Cyan
$mensaje = Read-Host "Ingresa el mensaje del commit (o presiona Enter para usar un mensaje por defecto)"
if ([string]::IsNullOrWhiteSpace($mensaje)) {
    $mensaje = "Actualización del proyecto"
}
git commit -m "$mensaje"
Write-Host "OK: Commit creado" -ForegroundColor Green
Write-Host ""

# Configurar rama
Write-Host "Configurando rama principal..." -ForegroundColor Yellow
git branch -M main
Write-Host "OK: Rama configurada como 'main'" -ForegroundColor Green
Write-Host ""

# Verificar si hay repositorio remoto
$remoteUrl = git remote get-url origin 2>$null

if (-not $remoteUrl) {
    Write-Host "No hay repositorio remoto configurado." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Opciones:" -ForegroundColor Cyan
    Write-Host "1. HTTPS (recomendado): https://github.com/USERNAME/REPO.git" -ForegroundColor White
    Write-Host "2. SSH: git@github.com:USERNAME/REPO.git" -ForegroundColor White
    Write-Host ""
    $url = Read-Host "Ingresa la URL de tu repositorio en GitHub"
    
    if ($url) {
        Write-Host "Conectando a GitHub..." -ForegroundColor Yellow
        git remote add origin "$url"
        Write-Host "OK: Repositorio remoto configurado" -ForegroundColor Green
        Write-Host ""
    } else {
        Write-Host "Operacion cancelada. Debes configurar el repositorio remoto." -ForegroundColor Red
        exit
    }
} else {
    Write-Host "Repositorio remoto encontrado: $remoteUrl" -ForegroundColor Green
    Write-Host ""
}

# Subir a GitHub
Write-Host "Subiendo a GitHub..." -ForegroundColor Cyan
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Subida exitosa a GitHub!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Tu repositorio esta en:" -ForegroundColor Yellow
    Write-Host "  $remoteUrl" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Error al subir. Verifica tu conexion a GitHub." -ForegroundColor Red
    Write-Host ""
}
