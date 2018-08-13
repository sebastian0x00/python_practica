from tkinter import *

root = Tk()

varOpcion = IntVar()

Label(root, text = "Género:").pack()

def imprimir():

	print(varOpcion.get())

Radiobutton(root, text = "Masculino", variable = varOpcion, value = 1, command = imprimir).pack()

Radiobutton(root, text = "Femenino", variable = varOpcion, value = 2, command = imprimir).pack()

root.mainloop()
