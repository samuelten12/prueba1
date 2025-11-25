import tkinter as tk  # importa tkinter con alias 'tk' para construir la interfaz gráfica
from tkinter import messagebox  # importa messagebox para mostrar diálogos emergentes


def show_text(event=None):  # función que muestra el texto ingresado (acepta un evento opcional)
    text = entry.get()  # obtiene el texto actual del widget Entry
    if text.strip() == "":  # comprueba si el texto está vacío o sólo contiene espacios
        messagebox.showwarning("Aviso", "No ingresó texto.")  # muestra una advertencia si está vacío
    else:
        messagebox.showinfo("Texto ingresado", text)  # muestra el texto ingresado en un diálogo informativo


root = tk.Tk()  # crea la ventana principal de la aplicación
root.title("Mostrar Texto")  # fija el título de la ventana
root.resizable(False, False)  # desactiva el redimensionado horizontal y vertical

frame = tk.Frame(root, padx=12, pady=12)  # crea un marco con padding para contener widgets
frame.pack()  # empaqueta el marco en la ventana principal

label = tk.Label(frame, text="Ingrese texto:")  # etiqueta que indica al usuario qué hacer
label.grid(row=0, column=0, sticky="w")  # coloca la etiqueta en la fila 0, columna 0 y la alinea a la izquierda

entry = tk.Entry(frame, width=40)  # campo de texto para la entrada del usuario
entry.grid(row=1, column=0, pady=(6, 10))  # coloca el Entry en la grilla con padding vertical
entry.focus()  # pone el foco en el Entry al iniciar la aplicación
entry.bind("<Return>", show_text)  # enlaza la tecla Enter para invocar show_text

button = tk.Button(frame, text="Mostrar", width=12, command=show_text)  # botón que ejecuta show_text al hacer clic
button.grid(row=2, column=0)  # coloca el botón en la fila 2, columna 0

root.mainloop()  # inicia el bucle principal de eventos de la interfaz
