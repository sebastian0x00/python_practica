from tkinter import *

raiz = Tk()

raiz.title("Hora del mate")

raiz.resizable(True, False) #width = ancho || height = alto -- 1 es igual a True, 0 a False

raiz.iconbitmap("mate.ico")

raiz.geometry("650x350")

raiz.config(bg = "green")

raiz.mainloop()
