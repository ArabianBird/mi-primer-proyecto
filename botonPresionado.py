import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")  # Tamaño de la ventana

# Agregar una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack(pady=20)

# Agregar un botón
def saludar():
    etiqueta.config(text="¡Botón presionado!")
boton = tk.Button(ventana, text="Clic aquí", command=saludar)
boton.pack()

# Iniciar el bucle principal
ventana.mainloop()