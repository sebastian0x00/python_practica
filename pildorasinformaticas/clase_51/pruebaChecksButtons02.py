from tkinter import *

root = Tk()

root.title("Ejemplo")

foto = PhotoImage(file="avion.png")
Label(root, image = foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destions", width = 50).pack()

Checkbutton(frame, text = "Playa").pack()
Checkbutton(frame, text = "Montaña").pack()
Checkbutton(frame, text = "Turismo Rural").pack()

root.mainloop()
