import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
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
        """
        atomos = defaultdict(int)
        formula = formula.replace(' ', '')
        patron = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(patron, formula)
        
        for elemento, cantidad in matches:
            if elemento not in self.atomos_permitidos:
                raise ValueError(f"Átomo no permitido: {elemento}. Solo se permiten: H, C, O, N")
            
            cantidad = int(cantidad) if cantidad else 1
            atomos[elemento] += cantidad
        
        return dict(atomos)
    
    def parsear_ecuacion(self, ecuacion):
        """Parsea una ecuación química."""
        ecuacion = ecuacion.replace(' ', '')
        
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
        """Cuenta los átomos en un conjunto de moléculas con coeficientes."""
        totales = defaultdict(int)
        
        for formula, coeficiente in moleculas:
            atomos = self.parsear_formula(formula)
            for elemento, cantidad in atomos.items():
                totales[elemento] += cantidad * coeficiente
        
        return dict(totales)
    
    def balancear(self, ecuacion, max_coeficiente=10):
        """Balancea una ecuación química por prueba y error."""
        try:
            reactivos, productos = self.parsear_ecuacion(ecuacion)
        except Exception as e:
            return f"Error: {e}"
        
        num_reactivos = len(reactivos)
        num_productos = len(productos)
        total_moleculas = num_reactivos + num_productos
        
        for coeficientes in product(range(1, max_coeficiente + 1), repeat=total_moleculas):
            coef_reactivos = coeficientes[:num_reactivos]
            coef_productos = coeficientes[num_reactivos:]
            
            moleculas_reactivos = list(zip(reactivos, coef_reactivos))
            moleculas_productos = list(zip(productos, coef_productos))
            
            atomos_reactivos = self.contar_atomos(moleculas_reactivos)
            atomos_productos = self.contar_atomos(moleculas_productos)
            
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
            return "No se pudo balancear la ecuación"
        
        if isinstance(resultado, str):
            return resultado
        
        reactivos, productos = resultado
        
        reactivos_str = ' + '.join([f"{coef if coef > 1 else ''}{formula}".strip() 
                                     for formula, coef in reactivos])
        productos_str = ' + '.join([f"{coef if coef > 1 else ''}{formula}".strip() 
                                     for formula, coef in productos])
        
        return f"{reactivos_str} → {productos_str}"


class BalanceadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Balanceador de Ecuaciones Químicas")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Configurar estilo
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use('clam')
        
        self.balanceador = BalanceadorEcuaciones()
        
        self.crear_widgets()
    
    def crear_widgets(self):
        """Crea los widgets de la interfaz"""
        
        # Marco principal
        marco_principal = ttk.Frame(self.root, padding="20")
        marco_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = tk.Label(marco_principal, text="Balanceador de Ecuaciones Químicas", 
                         font=("Arial", 20, "bold"), fg="#2c3e50", bg="#f0f0f0")
        titulo.pack(pady=(0, 10))
        
        # Subtítulo
        subtitulo = tk.Label(marco_principal, 
                            text="Átomos permitidos: H, C, O, N", 
                            font=("Arial", 10), fg="#7f8c8d", bg="#f0f0f0")
        subtitulo.pack(pady=(0, 20))
        
        # Marco de entrada
        marco_entrada = ttk.LabelFrame(marco_principal, text="Ecuación a Balancear", padding="10")
        marco_entrada.pack(fill=tk.X, pady=(0, 15))
        
        # Etiqueta de formato
        formato = tk.Label(marco_entrada, text="Formato: H2+O2->H2O  o  CH4+O2=CO2+H2O", 
                          font=("Arial", 9), fg="#95a5a6", bg="#f0f0f0")
        formato.pack(anchor=tk.W, pady=(0, 5))
        
        # Campo de entrada
        self.entrada_ecuacion = ttk.Entry(marco_entrada, font=("Arial", 12), width=60)
        self.entrada_ecuacion.pack(fill=tk.X, pady=(0, 10))
        self.entrada_ecuacion.bind("<Return>", lambda e: self.balancear_ecuacion())
        
        # Botones
        marco_botones = tk.Frame(marco_entrada, bg="#f0f0f0")
        marco_botones.pack(fill=tk.X)
        
        btn_balancear = ttk.Button(marco_botones, text="Balancear", 
                                   command=self.balancear_ecuacion)
        btn_balancear.pack(side=tk.LEFT, padx=(0, 10))
        
        btn_limpiar = ttk.Button(marco_botones, text="Limpiar", 
                                command=self.limpiar_campos)
        btn_limpiar.pack(side=tk.LEFT)
        
        # Marco de resultado
        marco_resultado = ttk.LabelFrame(marco_principal, text="Resultado", padding="10")
        marco_resultado.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.resultado_texto = scrolledtext.ScrolledText(marco_resultado, 
                                                          font=("Arial", 12, "bold"),
                                                          height=3, width=70,
                                                          bg="#ecf0f1", fg="#2c3e50",
                                                          relief=tk.FLAT, padx=10, pady=10)
        self.resultado_texto.pack(fill=tk.BOTH, expand=True)
        self.resultado_texto.config(state=tk.DISABLED)
        
        # Marco de ejemplos
        marco_ejemplos = ttk.LabelFrame(marco_principal, text="Ejemplos", padding="10")
        marco_ejemplos.pack(fill=tk.BOTH, expand=True)
        
        ejemplos = [
            ("H₂ + O₂ → H₂O", "H2+O2->H2O"),
            ("CH₄ + O₂ → CO₂ + H₂O", "CH4+O2->CO2+H2O"),
            ("C₂H₆ + O₂ → CO₂ + H₂O", "C2H6+O2->CO2+H2O"),
            ("N₂ + H₂ → NH₃", "N2+H2->NH3"),
            ("C₃H₈ + O₂ → CO₂ + H₂O", "C3H8+O2->CO2+H2O"),
            ("Fe + O₂ → Fe₂O₃", "Fe+O2->Fe2O3"),
        ]
        
        for texto, formula in ejemplos:
            # Solo mostrar ejemplos válidos
            if "Fe" not in formula:  # Fe no está permitido
                btn = ttk.Button(marco_ejemplos, text=texto, 
                               command=lambda f=formula: self.usar_ejemplo(f),
                               width=40)
                btn.pack(pady=2, padx=5, anchor=tk.W)
    
    def balancear_ecuacion(self):
        """Balancea la ecuación ingresada"""
        ecuacion = self.entrada_ecuacion.get().strip()
        
        if not ecuacion:
            messagebox.showwarning("Entrada vacía", "Por favor ingresa una ecuación")
            return
        
        resultado = self.balanceador.balancear(ecuacion)
        ecuacion_balanceada = self.balanceador.formatear_resultado(resultado)
        
        # Mostrar resultado
        self.resultado_texto.config(state=tk.NORMAL)
        self.resultado_texto.delete(1.0, tk.END)
        self.resultado_texto.insert(tk.END, ecuacion_balanceada)
        self.resultado_texto.config(state=tk.DISABLED)
        
        if resultado is None or isinstance(resultado, str):
            if "Error" in ecuacion_balanceada or "No se pudo" in ecuacion_balanceada:
                messagebox.showerror("Error", ecuacion_balanceada)
    
    def limpiar_campos(self):
        """Limpia todos los campos"""
        self.entrada_ecuacion.delete(0, tk.END)
        self.resultado_texto.config(state=tk.NORMAL)
        self.resultado_texto.delete(1.0, tk.END)
        self.resultado_texto.config(state=tk.DISABLED)
        self.entrada_ecuacion.focus()
    
    def usar_ejemplo(self, formula):
        """Usa un ejemplo como entrada"""
        self.entrada_ecuacion.delete(0, tk.END)
        self.entrada_ecuacion.insert(0, formula)
        self.balancear_ecuacion()


if __name__ == "__main__":
    root = tk.Tk()
    app = BalanceadorApp(root)
    root.mainloop()
