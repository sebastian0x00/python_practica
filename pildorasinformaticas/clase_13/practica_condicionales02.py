print("Asignaturasoptativas año 2017")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("informática gráfica",  "pruebas de software" , "usabilidad y accesibilidad"):
	print ("Asignatura elegida " + asignatura)
else:
	print("La asigntura escogida no está cotemplada")
