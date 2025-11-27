# Balanceador de Ecuaciones Quimicas

> Una aplicacion moderna e intuitiva para balancear ecuaciones quimicas de forma automatica.

![Estado](https://img.shields.io/badge/Estado-Funcional-green)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![Licencia](https://img.shields.io/badge/Licencia-Educativa-orange)
![Windows](https://img.shields.io/badge/SO-Windows%207%2B-0078D4)

---

## Tabla de Contenidos

- [Caracteristicas](#caracteristicas)
- [Requisitos](#requisitos)
- [Instalacion](#instalacion)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Documentacion](#documentacion)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Caracteristicas

OK Interfaz grafica moderna - Diseño limpio e intuitivo con Tkinter
OK Balancea automaticamente - Ecuaciones quimicas usando algoritmo de prueba y error
OK Validacion integrada - Solo permite atomos H, C, O, N
OK Botones de ejemplos - Prueba rapidamente con ecuaciones predefinidas
OK Sin instalacion - Ejecutable compilado, listo para usar
OK Sin dependencias externas - No requiere Python instalado
OK Multiplataforma Windows - Funciona en Windows 7, 8, 10, 11
OK Codigo abierto - Repositorio publico en GitHub

---

## Requisitos

### Para Ejecutable
- SO: Windows 7 o superior (32 bits o 64 bits)
- RAM: Minimo 512 MB
- Espacio: ~50 MB en disco
- Conexion: No requiere internet

### Para Version de Codigo Fuente
- Python: 3.7 o superior
- Dependencias: Librerias estandar de Python (re, itertools, collections, tkinter)

---

## Instalacion

### Opcion 1: Ejecutable (Recomendado)

Pasos:

1. Descargar el ejecutable desde la carpeta `dist/`:
   ```
   BalanceadorEcuaciones.exe
   ```

2. Doble clic en el archivo para ejecutar

3. Listo! La aplicacion se abrira inmediatamente

### Opcion 2: Desde Codigo Fuente

```powershell
# Instalar Python desde: https://www.python.org/downloads/
python app_gui.py
```

---

## Uso

### Pasos para Balancear

1. Ingresa una ecuacion en el campo de texto
   - Ejemplo: `H2+O2->H2O`

2. Presiona 'Balancear' o pulsa Enter

3. Lee el resultado en el area de salida
   - Ejemplo: `H2 + O2 -> H2O2`

4. Prueba otro ejemplo o presiona 'Limpiar'

---

## Ejemplos

### Ecuaciones Validas

| Descripcion | Formato | Resultado |
|-------------|---------|-----------|
| Combustion de H | `H2+O2->H2O` | `H2 + O2 -> H2O2` |
| Combustion de CH4 | `CH4+O2->CO2+H2O` | `CH4 + 2O2 -> CO2 + 2H2O` |
| Combustion de C2H6 | `C2H6+O2->CO2+H2O` | `2C2H6 + 7O2 -> 4CO2 + 6H2O` |
| Sintesis de NH3 | `N2+H2->NH3` | `N2 + 3H2 -> 2NH3` |
| Combustion de C3H8 | `C3H8+O2->CO2+H2O` | `C3H8 + 5O2 -> 3CO2 + 4H2O` |

### Ecuaciones NO Validas

| Ecuacion | Razon |
|----------|-------|
| `Fe+O2->Fe2O3` | Fe no esta permitido |
| `H2+O2` | Falta separador (-> o =) |
| `H2O->H2O` | Sin reactivos |
| `Na+Cl->NaCl` | Na y Cl no permitidos |

---

## Documentacion

Para informacion mas detallada, consulta:

- [ESPECIFICACIONES.md](./ESPECIFICACIONES.md) - Especificaciones tecnicas
- [INSTRUCCIONES_COMPILACION.md](./INSTRUCCIONES_COMPILACION.md) - Como compilar
- [GITHUB_SETUP.md](./GITHUB_SETUP.md) - Guia para GitHub

---

## Desarrollo

### Compilar desde Codigo Fuente

```powershell
pip install pyinstaller
pyinstaller --onefile --windowed --name="BalanceadorEcuaciones" app_gui.py
```

### Generar README Automaticamente

```powershell
python generar_readme.py
```

---

## Solucion de Problemas

### La aplicacion no abre
- Ejecuta como administrador
- Desactiva temporalmente el antivirus
- Verifica Windows 7 o superior

### Ecuacion no se balancea
- Verifica que solo uses: H, C, O, N
- Usa formato: `Reactivos->Productos`
- Ejemplo: `H2+O2->H2O`

---

## Licencia

Uso libre para propositos educativos.

Puedes:
- Usar la aplicacion
- Modificar el codigo
- Distribuir la aplicacion
- Usar en contextos educativos

---

## Contacto

- GitHub: https://github.com/samuelten12
- Repositorio: https://github.com/samuelten12/prueba1

---

Desarrollado con amor para estudiantes de quimica

*Balanceador de Ecuaciones Quimicas v1.0*
*Generado: 27 de November de 2025*