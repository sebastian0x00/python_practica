from tkinter import *

root = Tk()

varOpcion = IntVar()

Label(root, text = "Género:").pack()

def imprimir():

	#print(varOpcion.get())

	if varOpcion.get() == 1:

		etiqueta.config(text = "Has elegido masculino")

	elif varOpcion.get() == 2:

		etiqueta.config(text = "Has elegido feminino")

	else:
		etiqueta.config(text = "Has elegido otros")

Radiobutton(root, text = "Masculino", variable = varOpcion, value = 1, command = imprimir).pack()

Radiobutton(root, text = "Femenino", variable = varOpcion, value = 2, command = imprimir).pack()

Radiobutton(root, text = "Otras opciones", variable = varOpcion, value = 3, command = imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()



root.mainloop()
