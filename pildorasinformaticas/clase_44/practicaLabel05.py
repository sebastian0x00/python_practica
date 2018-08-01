from tkinter import *

root = Tk()

miFrame = Frame(root, width = 500, height = 400)

miFrame.pack()

miImagen = PhotoImage(file = "mouse.gif")

Label(miFrame, image = miImagen).place(x = 100, y = 200)

root.mainloop()
