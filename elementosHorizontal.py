""" import tkinter as tk

root = tk.Tk()

for i in range(3):
    tk.Button(text=f"{i}",command=lambda valor = i: print(valor)).pack()

root.mainloop() """

""" import tkinter as tk

root = tk.Tk()
root.title("Elementos en horizontal")

# Crear widgets
label = tk.Label(root, text="Etiqueta:")
text = tk.Text(root, height=1, width=20)
button = tk.Button(root, text="Botón")

# Alinear widgets en horizontal
label.pack(side="left", padx=5)
text.pack(side="left", padx=5)
button.pack(side="left", padx=5)

root.mainloop() """

import tkinter as tk

root = tk.Tk()
root.title("Elementos en horizontal")

# Crear widgets
label = tk.Label(root, text="Etiqueta:")
text = tk.Text(root, height=1, width=20)
button = tk.Button(root, text="Botón")

# Alinear widgets en horizontal (misma fila, columnas distintas)
label.grid(row=0, column=0, padx=5)
text.grid(row=0, column=1, padx=5)
button.grid(row=0, column=2, padx=5)

root.mainloop()