from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width = 1200, height = 600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row = 0, column = 1)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 1, column = 1)

cuadroDirrecion = Entry(miFrame)
cuadroDirrecion.grid(row = 2  , column = 1)

nombreLabel = Label(miFrame, text = "Nombre:")
nombreLabel.grid(row = 0, column = 0, sticky = "e") 

apellidoLabel = Label(miFrame, text = "Apellido:")
apellidoLabel.grid(row = 1, column = 0, sticky = "e") 

DirrecionLabel = Label(miFrame, text = "Dirreción de casa:")
DirrecionLabel.grid(row = 2, column = 0, sticky = "e") 

raiz.mainloop()
