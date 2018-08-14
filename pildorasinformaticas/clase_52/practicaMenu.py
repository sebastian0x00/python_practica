from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu)

archivoMenu = Menu(barraMenu)

archivoEdicion = Menu(barraMenu)

archivoHerramientas = Menu(barraMenu)

archivoAyuda = Menu(barraMenu)

root.mainloop()
