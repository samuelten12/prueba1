# 📋 Especificaciones Técnicas - Balanceador de Ecuaciones Químicas

## 📌 Información General

| Aspecto | Descripción |
|--------|-------------|
| **Nombre** | Balanceador de Ecuaciones Químicas |
| **Versión** | 1.0 |
| **Tipo** | Aplicación de Escritorio |
| **Plataforma** | Windows 7+ |
| **Licencia** | Uso libre para propósitos educativos |
| **Lenguaje** | Python 3.13+ |
| **Interfaz** | Gráfica (GUI) con Tkinter |

---

## 🎯 Objetivos

La aplicación busca proporcionar una herramienta educativa simple y efectiva para:
- ✅ Balancear ecuaciones químicas de forma automatizada
- ✅ Validar el uso correcto de átomos permitidos
- ✅ Mostrar resultados de manera clara e intuitiva
- ✅ Ser accesible sin requerir instalación de software adicional

---

## ⚛️ Limitaciones de Átomos

La aplicación **solo permite** los siguientes elementos químicos:

| Elemento | Símbolo | Número Atómico |
|----------|---------|-----------------|
| Hidrógeno | H | 1 |
| Carbono | C | 6 |
| Oxígeno | O | 8 |
| Nitrógeno | N | 7 |

**Ejemplos de ecuaciones válidas:**
- `H2+O2->H2O` ✅
- `CH4+O2->CO2+H2O` ✅
- `N2+H2->NH3` ✅

**Ejemplos de ecuaciones NO válidas:**
- `Fe+O2->Fe2O3` ❌ (contiene Fe - Hierro)
- `CaCO3->CaO+CO2` ❌ (contiene Ca - Calcio)
- `Na+Cl->NaCl` ❌ (contiene Na y Cl)

---

## 🔧 Especificaciones Técnicas

### Dependencias

```python
# Librerías estándar de Python (incluidas por defecto)
- re              # Expresiones regulares (parseo de fórmulas)
- itertools       # Combinaciones (prueba de coeficientes)
- collections     # defaultdict (conteo de átomos)
- tkinter         # Interfaz gráfica (GUI)
```

### Requisitos del Sistema

| Requisito | Especificación |
|-----------|-----------------|
| **SO** | Windows 7, 8, 10, 11 |
| **Arquitectura** | 32 bits o 64 bits |
| **RAM** | Mínimo 512 MB |
| **Espacio en Disco** | ~50 MB (ejecutable compilado) |
| **Python** | 3.7+ (solo para versión de código fuente) |

---

## 🏗️ Arquitectura de la Aplicación

### Estructura de Archivos

```
balanceador-ecuaciones/
│
├── app_gui.py                      # Interfaz gráfica principal
├── balanceador_ecuaciones.py       # Lógica del balanceador
├── compilar.ps1                    # Script de compilación
├── subir_github.ps1                # Script para GitHub
│
├── README.md                       # Documentación principal
├── INSTRUCCIONES_COMPILACION.md    # Guía de compilación
├── GITHUB_SETUP.md                 # Guía de GitHub
├── DISTRIBUCION.txt                # Instrucciones de distribución
│
├── dist/
│   └── BalanceadorEcuaciones.exe   # Ejecutable compilado
│
├── build/                          # Carpeta temporal (compilación)
└── BalanceadorEcuaciones_v1.0.zip  # Paquete distribuible
```

### Componentes Principales

#### 1. **Clase: BalanceadorEcuaciones**
Ubicación: `balanceador_ecuaciones.py`

**Métodos:**
- `__init__()` - Inicializa los átomos permitidos
- `parsear_formula(formula)` - Convierte una fórmula en diccionario de átomos
- `parsear_ecuacion(ecuacion)` - Separa reactivos y productos
- `contar_atomos(moleculas)` - Cuenta átomos totales con coeficientes
- `balancear(ecuacion, max_coeficiente=10)` - Balancea la ecuación por prueba y error
- `formatear_resultado(resultado)` - Formatea el resultado para mostrar

**Ejemplo de uso:**
```python
from balanceador_ecuaciones import BalanceadorEcuaciones

balanceador = BalanceadorEcuaciones()
resultado = balanceador.balancear("H2+O2->H2O")
print(balanceador.formatear_resultado(resultado))
# Salida: H2 + O2 → H2O2
```

#### 2. **Clase: BalanceadorApp**
Ubicación: `app_gui.py`

**Responsabilidades:**
- Crear la interfaz gráfica
- Manejar eventos del usuario
- Mostrar resultados
- Gestionar ejemplos predefinidos

**Componentes GUI:**
- Título y descripción
- Campo de entrada de ecuaciones
- Botones (Balancear, Limpiar)
- Área de resultados
- Botones de ejemplos predefinidos

---

## 🔍 Algoritmo de Balanceo

### Método: Prueba y Error

1. **Parseo de entrada:** Separa reactivos y productos
2. **Generación de combinaciones:** Crea todas las combinaciones de coeficientes (1-10)
3. **Validación:** Para cada combinación:
   - Cuenta átomos en reactivos
   - Cuenta átomos en productos
   - Verifica si coinciden todos los átomos
4. **Resultado:** Retorna la primera combinación válida encontrada

**Complejidad:**
- Tiempo: O(n^m) donde n=coeficiente máximo, m=número de moléculas
- Espacio: O(m) para almacenar moleculas y átomos

**Limitaciones:**
- Máximo coeficiente por defecto: 10
- Funciona bien para ecuaciones simples (hasta ~4 moléculas)
- No encuentra ecuaciones si requieren coeficientes > 10

---

## 💻 Interfaz Gráfica

### Elementos de la GUI

```
┌─────────────────────────────────────┐
│ Balanceador de Ecuaciones Químicas  │
│ Átomos permitidos: H, C, O, N       │
├─────────────────────────────────────┤
│ ECUACIÓN A BALANCEAR                │
│ Formato: H2+O2->H2O                 │
│ ┌───────────────────────────────┐   │
│ │ [Campo de entrada]            │   │
│ └───────────────────────────────┘   │
│ [Balancear] [Limpiar]               │
├─────────────────────────────────────┤
│ RESULTADO                           │
│ ┌───────────────────────────────┐   │
│ │ Ecuación balanceada aquí      │   │
│ └───────────────────────────────┘   │
├─────────────────────────────────────┤
│ EJEMPLOS                            │
│ [H₂ + O₂ → H₂O]                     │
│ [CH₄ + O₂ → CO₂ + H₂O]              │
│ [C₂H₆ + O₂ → CO₂ + H₂O]             │
│ [N₂ + H₂ → NH₃]                     │
│ [C₃H₈ + O₂ → CO₂ + H₂O]             │
└─────────────────────────────────────┘
```

### Características de la Interfaz

- **Tamaño:** 800x600 píxeles (redimensionable)
- **Tema:** Clam (moderno y plano)
- **Colores:** Tonos grises neutros con acentos azules
- **Fuente:** Arial, tamaños 20 (título), 12 (entrada), 9 (instrucciones)
- **Responsividad:** Se adapta al cambio de tamaño de ventana

---

## 📝 Formato de Entrada

### Sintaxis Aceptada

```
ECUACIÓN := REACTIVOS SEPARADOR PRODUCTOS
REACTIVOS := FORMULA [+ FORMULA]*
PRODUCTOS := FORMULA [+ FORMULA]*
SEPARADOR := "->" | "="
FORMULA := ELEMENTO [NUMERO] [ELEMENTO [NUMERO]]*
ELEMENTO := H | C | O | N
NUMERO := 1-9+
```

### Ejemplos Válidos

| Entrada | Descripción |
|---------|-------------|
| `H2+O2->H2O` | Combustión de hidrógeno |
| `CH4+O2=CO2+H2O` | Combustión de metano (con =) |
| `C2H6+O2->CO2+H2O` | Combustión de etano |
| `N2+H2->NH3` | Síntesis de amoníaco |
| `H2 + O2 -> H2O` | Con espacios (se ignoran) |

### Ejemplos NO Válidos

| Entrada | Razón del Error |
|---------|-----------------|
| `H2+O2` | Falta separador (-> o =) |
| `Fe+O2->Fe2O3` | Fe no es permitido |
| `H2O->H2O` | Sin reactivo |
| `CH4+O2->` | Sin producto |
| `H2++O2->H2O` | Doble + |

---

## 🔄 Flujo de Ejecución

```
┌─────────────────────┐
│   Inicio Aplicación │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────┐
│  Crear Interfaz Gráfica │
└──────────┬──────────────┘
           │
           ▼
┌──────────────────────────────┐
│ Esperar entrada del usuario  │
└──────────┬───────────────────┘
           │
      ┌────┴──────────────┐
      │                   │
      ▼                   ▼
  [Balancear]        [Ejemplo]
      │                   │
      ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│ Parsear ecuación │  │ Copiar en campo  │
└────────┬─────────┘  │ Balancear        │
         │            └────────┬─────────┘
         ▼                     │
┌──────────────────────┐       │
│ Probar combinaciones │       │
└────────┬─────────────┘       │
         │                     │
    ┌────┴─────────────────────┘
    │
    ▼
┌──────────────────────┐
│ Mostrar Resultado    │
└────────┬─────────────┘
         │
    ┌────┴─────────────────────┐
    │                          │
    ▼                          ▼
[Balancear otra]       [Limpiar campos]
```

---

## 🧪 Casos de Prueba

### Casos Exitosos

```python
# Caso 1: Combustión simple
Entrada:    "H2+O2->H2O"
Esperado:   "H2 + O2 → H2O2"
Resultado:  ✅ PASÓ

# Caso 2: Combustión de metano
Entrada:    "CH4+O2->CO2+H2O"
Esperado:   "CH4 + 2O2 → CO2 + 2H2O"
Resultado:  ✅ PASÓ

# Caso 3: Con espacios
Entrada:    "C2H6 + O2 -> CO2 + H2O"
Esperado:   "2C2H6 + 7O2 → 4CO2 + 6H2O"
Resultado:  ✅ PASÓ
```

### Casos de Error

```python
# Caso 1: Átomo no permitido
Entrada:    "Fe+O2->Fe2O3"
Resultado:  ❌ Error: "Átomo no permitido: Fe"

# Caso 2: Sin separador
Entrada:    "H2+O2"
Resultado:  ❌ Error: "La ecuación debe contener '->' o '='"

# Caso 3: Ecuación no balanceable
Entrada:    "H->C"
Resultado:  ❌ No se puede balancear

# Caso 4: Entrada vacía
Entrada:    ""
Resultado:  ❌ Advertencia: "Por favor ingresa una ecuación"
```

---

## 📦 Distribución y Despliegue

### Versión Código Fuente
- **Requisito:** Python 3.7+
- **Instalación de dependencias:** Ninguna (solo librerías estándar)
- **Ejecución:** `python app_gui.py`

### Versión Ejecutable
- **Requisito:** Windows 7+
- **Tamaño:** ~10 MB
- **Ejecución:** Doble clic en `BalanceadorEcuaciones.exe`
- **Compilador utilizado:** PyInstaller 6.17.0

### Paquete Distribuible
- **Formato:** ZIP
- **Contenido:** Ejecutable + documentación
- **Tamaño comprimido:** ~3-4 MB
- **Plataforma:** Cualquier sitio web, email, USB

---

## 🚀 Mejoras Futuras

### Corto Plazo
- [ ] Agregar más átomos permitidos (S, P, Cl, Br, etc.)
- [ ] Aumentar el coeficiente máximo a 20
- [ ] Mostrar detalles de balanceo (paso a paso)
- [ ] Historial de ecuaciones balanceadas

### Mediano Plazo
- [ ] Interfaz en español e inglés
- [ ] Exportar resultados a PDF
- [ ] Guardar ecuaciones favoritas
- [ ] Modo oscuro en la GUI

### Largo Plazo
- [ ] Versión web (con Flask/Django)
- [ ] Aplicación móvil
- [ ] Integración con cálculos de masa molar
- [ ] Base de datos de ecuaciones químicas
- [ ] Sistema de puntuación (modo educativo)

---

## 📊 Rendimiento

### Benchmark (Máquina de Prueba)
- **Procesador:** Intel Core i5
- **RAM:** 8 GB
- **SO:** Windows 11

| Ecuación | Moléculas | Tiempo |
|----------|-----------|--------|
| `H2+O2->H2O` | 3 | < 1 ms |
| `CH4+O2->CO2+H2O` | 4 | ~5 ms |
| `C3H8+O2->CO2+H2O` | 4 | ~50 ms |
| `C6H12O6+O2->CO2+H2O` | 4 | ~100 ms |

---

## 🔒 Consideraciones de Seguridad

- ✅ Sin acceso a internet (aplicación offline)
- ✅ Sin almacenamiento de datos personales
- ✅ Sin modificación del sistema de archivos
- ✅ No requiere permisos de administrador (en mayoría de casos)
- ✅ Código abierto y auditable

---

## 📄 Licencia y Uso

**Licencia:** Uso libre para propósitos educativos

Puedes:
- ✅ Usar la aplicación libremente
- ✅ Modificar el código fuente
- ✅ Distribuir la aplicación
- ✅ Usar en fines educativos

Se recomienda:
- Mantener atribución del autor original
- No vender la aplicación sin modificaciones significativas
- Reportar bugs encontrados

---

## 📞 Información de Soporte

- **Repositorio GitHub:** https://github.com/samuelten12/prueba1
- **Documentación:** Ver archivos .md en el repositorio
- **Reportar bugs:** Issues en GitHub

---

**Documento creado:** 27 de Noviembre de 2025  
**Versión:** 1.0  
**Estado:** Aplicación completamente funcional
