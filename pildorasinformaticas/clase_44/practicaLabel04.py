from tkinter import *

root = Tk()

miFrame = Frame(root, width = 500, height = 400)

miFrame.pack()

Label(miFrame, text = "Hola alumnos de Python", fg = "red", font = ("Comic Ssans MS", 18)).place(x = 100, y = 200)

root.mainloop()
