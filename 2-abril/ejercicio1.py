# tkinter -> creación y el desarrollo de aplicaciones de escritorio.
# tkinter -> es mas facil trabajar on GRID.

from tkinter import *
from tkinter import ttk


def imprimir_mensaje():
    print("hola a todos")

ventana = Tk()
ventana.geometry("300x200")
ventana.configure(bg = "beige")
ventana.title("Mi primera ventana")

ttk.Button(ventana, text = "Imprimir manesaje", command = imprimir_mensaje).pack(side = LEFT)

ttk.Button(ventana, text = "cerrar aplicacion", command = quit).pack(side = RIGHT)

entrada_texto = Entry(ventana).pack(side = BOTTOM)

ventana.mainloop()
