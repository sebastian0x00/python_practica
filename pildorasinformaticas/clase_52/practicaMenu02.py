from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu)

archivoMenu = Menu(barraMenu)

archivoEdicion = Menu(barraMenu)

archivoHerramientas = Menu(barraMenu)

archivoAyuda = Menu(barraMenu)

barraMenu.add_cascade(label = "archivo", menu = archivoMenu)

root.mainloop()
