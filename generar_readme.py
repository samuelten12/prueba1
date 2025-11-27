#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador automatico de README.md
Extrae informacion del codigo y genera documentacion completa
"""

from datetime import datetime

class GeneradorREADME:
    """Genera README.md automaticamente desde el codigo"""
    
    def __init__(self):
        self.titulo = "Balanceador de Ecuaciones Quimicas"
        self.version = "1.0"
        self.fecha = datetime.now().strftime("%d de %B de %Y")
        self.atomos = "H, C, O, N"
        self.ejemplos = [
            ("Combustion de H", "H2+O2->H2O", "H2 + O2 -> H2O2"),
            ("Combustion de CH4", "CH4+O2->CO2+H2O", "CH4 + 2O2 -> CO2 + 2H2O"),
            ("Combustion de C2H6", "C2H6+O2->CO2+H2O", "2C2H6 + 7O2 -> 4CO2 + 6H2O"),
            ("Sintesis de NH3", "N2+H2->NH3", "N2 + 3H2 -> 2NH3"),
            ("Combustion de C3H8", "C3H8+O2->CO2+H2O", "C3H8 + 5O2 -> 3CO2 + 4H2O"),
        ]
    
    def generar_readme(self):
        """Genera el contenido completo del README.md"""
        
        lineas = []
        
        # Encabezado
        lineas.append("# Balanceador de Ecuaciones Quimicas")
        lineas.append("")
        lineas.append("> Una aplicacion moderna e intuitiva para balancear ecuaciones quimicas de forma automatica.")
        lineas.append("")
        lineas.append("![Estado](https://img.shields.io/badge/Estado-Funcional-green)")
        lineas.append("![Version](https://img.shields.io/badge/Version-" + self.version + "-blue)")
        lineas.append("![Licencia](https://img.shields.io/badge/Licencia-Educativa-orange)")
        lineas.append("![Windows](https://img.shields.io/badge/SO-Windows%207%2B-0078D4)")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Tabla de Contenidos")
        lineas.append("")
        lineas.append("- [Caracteristicas](#caracteristicas)")
        lineas.append("- [Requisitos](#requisitos)")
        lineas.append("- [Instalacion](#instalacion)")
        lineas.append("- [Uso](#uso)")
        lineas.append("- [Ejemplos](#ejemplos)")
        lineas.append("- [Documentacion](#documentacion)")
        lineas.append("- [Contribuciones](#contribuciones)")
        lineas.append("- [Licencia](#licencia)")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Caracteristicas")
        lineas.append("")
        lineas.append("OK Interfaz grafica moderna - Diseño limpio e intuitivo con Tkinter")
        lineas.append("OK Balancea automaticamente - Ecuaciones quimicas usando algoritmo de prueba y error")
        lineas.append("OK Validacion integrada - Solo permite atomos " + self.atomos)
        lineas.append("OK Botones de ejemplos - Prueba rapidamente con ecuaciones predefinidas")
        lineas.append("OK Sin instalacion - Ejecutable compilado, listo para usar")
        lineas.append("OK Sin dependencias externas - No requiere Python instalado")
        lineas.append("OK Multiplataforma Windows - Funciona en Windows 7, 8, 10, 11")
        lineas.append("OK Codigo abierto - Repositorio publico en GitHub")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Requisitos")
        lineas.append("")
        lineas.append("### Para Ejecutable")
        lineas.append("- SO: Windows 7 o superior (32 bits o 64 bits)")
        lineas.append("- RAM: Minimo 512 MB")
        lineas.append("- Espacio: ~50 MB en disco")
        lineas.append("- Conexion: No requiere internet")
        lineas.append("")
        lineas.append("### Para Version de Codigo Fuente")
        lineas.append("- Python: 3.7 o superior")
        lineas.append("- Dependencias: Librerias estandar de Python (re, itertools, collections, tkinter)")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Instalacion")
        lineas.append("")
        lineas.append("### Opcion 1: Ejecutable (Recomendado)")
        lineas.append("")
        lineas.append("Pasos:")
        lineas.append("")
        lineas.append("1. Descargar el ejecutable desde la carpeta `dist/`:")
        lineas.append("   ```")
        lineas.append("   BalanceadorEcuaciones.exe")
        lineas.append("   ```")
        lineas.append("")
        lineas.append("2. Doble clic en el archivo para ejecutar")
        lineas.append("")
        lineas.append("3. Listo! La aplicacion se abrira inmediatamente")
        lineas.append("")
        lineas.append("### Opcion 2: Desde Codigo Fuente")
        lineas.append("")
        lineas.append("```powershell")
        lineas.append("# Instalar Python desde: https://www.python.org/downloads/")
        lineas.append("python app_gui.py")
        lineas.append("```")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Uso")
        lineas.append("")
        lineas.append("### Pasos para Balancear")
        lineas.append("")
        lineas.append("1. Ingresa una ecuacion en el campo de texto")
        lineas.append("   - Ejemplo: `H2+O2->H2O`")
        lineas.append("")
        lineas.append("2. Presiona 'Balancear' o pulsa Enter")
        lineas.append("")
        lineas.append("3. Lee el resultado en el area de salida")
        lineas.append("   - Ejemplo: `H2 + O2 -> H2O2`")
        lineas.append("")
        lineas.append("4. Prueba otro ejemplo o presiona 'Limpiar'")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Ejemplos")
        lineas.append("")
        lineas.append("### Ecuaciones Validas")
        lineas.append("")
        lineas.append("| Descripcion | Formato | Resultado |")
        lineas.append("|-------------|---------|-----------|")
        
        for desc, formato, resultado in self.ejemplos:
            lineas.append("| " + desc + " | `" + formato + "` | `" + resultado + "` |")
        
        lineas.append("")
        lineas.append("### Ecuaciones NO Validas")
        lineas.append("")
        lineas.append("| Ecuacion | Razon |")
        lineas.append("|----------|-------|")
        lineas.append("| `Fe+O2->Fe2O3` | Fe no esta permitido |")
        lineas.append("| `H2+O2` | Falta separador (-> o =) |")
        lineas.append("| `H2O->H2O` | Sin reactivos |")
        lineas.append("| `Na+Cl->NaCl` | Na y Cl no permitidos |")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Documentacion")
        lineas.append("")
        lineas.append("Para informacion mas detallada, consulta:")
        lineas.append("")
        lineas.append("- [ESPECIFICACIONES.md](./ESPECIFICACIONES.md) - Especificaciones tecnicas")
        lineas.append("- [INSTRUCCIONES_COMPILACION.md](./INSTRUCCIONES_COMPILACION.md) - Como compilar")
        lineas.append("- [GITHUB_SETUP.md](./GITHUB_SETUP.md) - Guia para GitHub")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Desarrollo")
        lineas.append("")
        lineas.append("### Compilar desde Codigo Fuente")
        lineas.append("")
        lineas.append("```powershell")
        lineas.append("pip install pyinstaller")
        lineas.append("pyinstaller --onefile --windowed --name=\"BalanceadorEcuaciones\" app_gui.py")
        lineas.append("```")
        lineas.append("")
        lineas.append("### Generar README Automaticamente")
        lineas.append("")
        lineas.append("```powershell")
        lineas.append("python generar_readme.py")
        lineas.append("```")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Solucion de Problemas")
        lineas.append("")
        lineas.append("### La aplicacion no abre")
        lineas.append("- Ejecuta como administrador")
        lineas.append("- Desactiva temporalmente el antivirus")
        lineas.append("- Verifica Windows 7 o superior")
        lineas.append("")
        lineas.append("### Ecuacion no se balancea")
        lineas.append("- Verifica que solo uses: " + self.atomos)
        lineas.append("- Usa formato: `Reactivos->Productos`")
        lineas.append("- Ejemplo: `H2+O2->H2O`")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Licencia")
        lineas.append("")
        lineas.append("Uso libre para propositos educativos.")
        lineas.append("")
        lineas.append("Puedes:")
        lineas.append("- Usar la aplicacion")
        lineas.append("- Modificar el codigo")
        lineas.append("- Distribuir la aplicacion")
        lineas.append("- Usar en contextos educativos")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("## Contacto")
        lineas.append("")
        lineas.append("- GitHub: https://github.com/samuelten12")
        lineas.append("- Repositorio: https://github.com/samuelten12/prueba1")
        lineas.append("")
        lineas.append("---")
        lineas.append("")
        lineas.append("Desarrollado con amor para estudiantes de quimica")
        lineas.append("")
        lineas.append("*Balanceador de Ecuaciones Quimicas v" + self.version + "*")
        lineas.append("*Generado: " + self.fecha + "*")
        
        return "\n".join(lineas)
    
    def guardar_readme(self, contenido, ruta="README.md"):
        """Guarda el README.md en el archivo especificado"""
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print("OK: README.md generado en: " + ruta)
        print("Tamaño: " + str(len(contenido)) + " caracteres")


def main():
    """Funcion principal"""
    print("=" * 60)
    print("GENERADOR AUTOMATICO DE README.md")
    print("=" * 60)
    print()
    
    # Crear generador
    generador = GeneradorREADME()
    
    # Generar README
    print("Generando README.md...")
    contenido = generador.generar_readme()
    
    # Guardar archivo
    ruta_readme = "README.md"
    generador.guardar_readme(contenido, ruta_readme)
    
    print()
    print("=" * 60)
    print("Proceso completado!")
    print("=" * 60)


if __name__ == "__main__":
    main()
