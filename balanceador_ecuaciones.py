import re
from itertools import product
from collections import defaultdict

class BalanceadorEcuaciones:
    """Balanceador de ecuaciones químicas para H, C, O, N"""
    
    def __init__(self):
        self.atomos_permitidos = {'H', 'C', 'O', 'N'}
    
    def parsear_formula(self, formula):
        """
        Parsea una fórmula química y retorna un diccionario con los átomos.
        Ejemplo: "H2O" -> {'H': 2, 'O': 1}
        """
        atomos = defaultdict(int)
        
        # Remover espacios
        formula = formula.replace(' ', '')
        
        # Patrón para encontrar elemento + número
        patron = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(patron, formula)
        
        for elemento, cantidad in matches:
            if elemento not in self.atomos_permitidos:
                raise ValueError(f"Átomo no permitido: {elemento}. Solo se permiten: H, C, O, N")
            
            cantidad = int(cantidad) if cantidad else 1
            atomos[elemento] += cantidad
        
        return dict(atomos)
    
    def parsear_ecuacion(self, ecuacion):
        """
        Parsea una ecuación química.
        Formato: "H2+O2->H2O" o "H2 + O2 -> H2O"
        Retorna (reactivos, productos) donde cada uno es lista de fórmulas
        """
        # Normalizar espacios y separadores
        ecuacion = ecuacion.replace(' ', '')
        
        # Separar reactivos y productos
        if '->' not in ecuacion and '=' not in ecuacion:
            raise ValueError("La ecuación debe contener '->' o '='")
        
        if '->' in ecuacion:
            reactivos_str, productos_str = ecuacion.split('->')
        else:
            reactivos_str, productos_str = ecuacion.split('=')
        
        reactivos = [f.strip() for f in reactivos_str.split('+')]
        productos = [f.strip() for f in productos_str.split('+')]
        
        return reactivos, productos
    
    def contar_atomos(self, moleculas):
        """
        Cuenta los átomos en un conjunto de moléculas con coeficientes.
        moleculas: lista de tuplas (fórmula, coeficiente)
        Retorna: diccionario {átomo: total_conteo}
        """
        totales = defaultdict(int)
        
        for formula, coeficiente in moleculas:
            atomos = self.parsear_formula(formula)
            for elemento, cantidad in atomos.items():
                totales[elemento] += cantidad * coeficiente
        
        return dict(totales)
    
    def balancear(self, ecuacion, max_coeficiente=10):
        """
        Balancea una ecuación química por prueba y error.
        max_coeficiente: coeficiente máximo a probar (por defecto 10)
        Retorna: (reactivos_balanceados, productos_balanceados) o None si no puede balancear
        """
        try:
            reactivos, productos = self.parsear_ecuacion(ecuacion)
        except Exception as e:
            return f"Error al parsear la ecuación: {e}"
        
        num_reactivos = len(reactivos)
        num_productos = len(productos)
        total_moleculas = num_reactivos + num_productos
        
        # Probar todas las combinaciones de coeficientes
        for coeficientes in product(range(1, max_coeficiente + 1), repeat=total_moleculas):
            coef_reactivos = coeficientes[:num_reactivos]
            coef_productos = coeficientes[num_reactivos:]
            
            # Contar átomos en reactivos y productos
            moleculas_reactivos = list(zip(reactivos, coef_reactivos))
            moleculas_productos = list(zip(productos, coef_productos))
            
            atomos_reactivos = self.contar_atomos(moleculas_reactivos)
            atomos_productos = self.contar_atomos(moleculas_productos)
            
            # Verificar si está balanceado
            todos_atomos = set(atomos_reactivos.keys()) | set(atomos_productos.keys())
            
            balanceado = True
            for atomo in todos_atomos:
                if atomos_reactivos.get(atomo, 0) != atomos_productos.get(atomo, 0):
                    balanceado = False
                    break
            
            if balanceado:
                resultado_reactivos = list(zip(reactivos, coef_reactivos))
                resultado_productos = list(zip(productos, coef_productos))
                return resultado_reactivos, resultado_productos
        
        return None
    
    def formatear_resultado(self, resultado):
        """Formatea el resultado de forma legible"""
        if resultado is None:
            return "No se pudo balancear la ecuación (intenta aumentando max_coeficiente)"
        
        if isinstance(resultado, str):
            return resultado
        
        reactivos, productos = resultado
        
        # Construir ecuación balanceada
        reactivos_str = ' + '.join([f"{coef if coef > 1 else ''}{formula}".strip() 
                                     for formula, coef in reactivos])
        productos_str = ' + '.join([f"{coef if coef > 1 else ''}{formula}".strip() 
                                     for formula, coef in productos])
        
        ecuacion_balanceada = f"{reactivos_str} -> {productos_str}"
        return ecuacion_balanceada


def main():
    balanceador = BalanceadorEcuaciones()
    
    print("=" * 60)
    print("BALANCEADOR DE ECUACIONES QUÍMICAS")
    print("Átomos permitidos: H (Hidrógeno), C (Carbono), O (Oxígeno), N (Nitrógeno)")
    print("=" * 60)
    print()
    
    while True:
        print("Ingresa una ecuación química (ej: H2+O2->H2O o escribe 'salir' para terminar):")
        ecuacion = input(">>> ").strip()
        
        if ecuacion.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not ecuacion:
            print("Por favor, ingresa una ecuación válida.\n")
            continue
        
        resultado = balanceador.balancear(ecuacion)
        ecuacion_balanceada = balanceador.formatear_resultado(resultado)
        
        print()
        print("Ecuación balanceada:")
        print(f"  {ecuacion_balanceada}")
        print()


if __name__ == "__main__":
    main()
