from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu)

archivoMenu.add_command(label = "Nuevo")

archivoMenu.add_command(label = "Guardar")

archivoMenu.add_command(label = "Guardar como")

archivoMenu.add_command(label = "Cerrar")

archivoMenu.add_command(label = "Salir")

archivoEdicion = Menu(barraMenu)

archivoHerramientas = Menu(barraMenu)

archivoAyuda = Menu(barraMenu)

barraMenu.add_cascade(label = "archivo", menu = archivoMenu)

barraMenu.add_cascade(label = "Edición", menu = archivoEdicion)

barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)

barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)

root.mainloop()
