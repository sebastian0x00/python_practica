print("Verificación de acceso")
nota_alumno = int(input("Introduce tu nota, por favor"))

if nota_alumno<5:
    print("Insuficiente")

elif nota_alumno<6:
    print("suficiente")

elif nota_alumno<7:
    print("Muy bien")

elif nota_alumno<9:
    print("Nota")

else:
    print("Sobresaliente")
