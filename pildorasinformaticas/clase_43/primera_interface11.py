from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(True, False) 

raiz.iconbitmap("mate.ico")

#raiz.geometry("650x350")

raiz.config(bg = "blue")

miFrame = Frame()

miFrame.pack()

miFrame.config(bg = "red")

miFrame.config(width = "650", height = "350")

miFrame.config(bd = 35)

miFrame.config(relief = "sunken")

miFrame.config(cursor = "pirate")

raiz.mainloop()