from tkinter import *

root = Tk()

miFrame = Frame(root, width = 500, height = 400)

miFrame.pack()

miLabel = Label(miFrame, text = "Hola alumnos de Python")

miLabel.place(x = 100, y = 200)

root.mainloop()
