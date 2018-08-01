from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(True, False) 

raiz.iconbitmap("mate.ico")

raiz.geometry("650x350")

raiz.config(bg = "blue")

miFrame = Frame()

miFrame.pack()

raiz.mainloop()
