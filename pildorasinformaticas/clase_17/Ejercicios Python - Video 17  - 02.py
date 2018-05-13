#Ejercicio 2:
#Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. Finalmente el programa muestras la suma de todos los números introducidos

numero = int(input("Introduce un número: "))
suma = 0

while numero > 0:
	suma = suma + numero
	numero = int(input("introduce otro numero: "))

print("La suma de los números introducidos es", str(suma))
