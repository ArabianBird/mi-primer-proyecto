""" import tkinter as tk

def copy_to_clipboard():
    Copia el contenido del widget Text al portapapeles.
    root.clipboard_clear()  # Limpia el portapapeles
    root.clipboard_append(text_widget.get("1.0", tk.END).rstrip())  # Copia el texto, eliminando el salto de línea final
    #print("Texto copiado al portapapeles!")  # Mensaje de confirmación (opcional)

# Crear la ventana principal
root = tk.Tk()
root.title("Copiar texto con un clic")
root.geometry("400x200")

# Crear un widget Text para mostrar el texto
text_widget = tk.Text(root, height=5, width=30)
text_widget.insert(tk.END, "¡Este es el texto que se copiará!")
text_widget.pack(pady=10)

# Crear un botón que copia el texto con un clic
copy_button = tk.Button(root, text="Copiar texto", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Iniciar el bucle principal
root.mainloop() """

import tkinter as tk

ventana = tk.Tk()

def bloquear_movimiento(event):
    ventana.geometry("-1-30")  # Forzar posición fija

ventana.title("Clave de Sol")
ventana.geometry("370x150-1-30")
ventana.bind("<Configure>", bloquear_movimiento)  # Detecta cambios en posición

""" frame_main = tk.Frame(ventana, bg="lightgray", bd=2, relief="ridge")
frame_main.pack(padx=10, pady=10, fill="both", expand=False) """


etiqueta01 = tk.Label(ventana, text="R")
etiqueta01.config(fg="black", bg="azure", font=("Arial", 14, "italic"))
etiqueta01.grid(row=0, column=0, padx=5)

text_widget01 = tk.Text(ventana, height=1, width=30)
text_widget01.insert(tk.END, "")
text_widget01.grid(row=0, column=1, padx=5)

boton01 = tk.Button(ventana, text=" ")
boton01.config(fg="black", bg="gainsboro", font=("Arial", 14, "italic"))
boton01.grid(row=0, column=2, padx=5)


etiqueta02 = tk.Label(ventana, text="U")
etiqueta02.config(fg="black", bg="azure", font=("Arial", 14, "italic"))
etiqueta02.grid(row=1, column=0, padx=5)

text_widget02 = tk.Text(ventana, height=1, width=30)
text_widget02.insert(tk.END, "")
text_widget02.grid(row=1, column=1, padx=5)

boton02 = tk.Button(ventana, text=" ")
boton02.config(fg="black", bg="gainsboro", font=("Arial", 14, "italic"))
boton02.grid(row=1, column=2, padx=5)


etiqueta03 = tk.Label(ventana, text="C")
etiqueta03.config(fg="black", bg="azure", font=("Arial", 14, "italic"))
etiqueta03.grid(row=2, column=0, padx=5)

text_widget03 = tk.Text(ventana, height=1, width=30)
text_widget03.insert(tk.END, "")
text_widget03.grid(row=2, column=1, padx=5)

boton03 = tk.Button(ventana, text=" ")
boton03.config(fg="black", bg="gainsboro", font=("Arial", 14, "italic"))
boton03.grid(row=2, column=2, padx=5)


def cambiar_texto():
    text_widget02.config(text="¡Boton!")

boton02.config(command=cambiar_texto)


ventana.mainloop()