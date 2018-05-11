#Ejercicio 2:
#Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, el programa imprime "Contraseña OK". En caso contarario imprime "Contraseña errónea"


contra = input("Introduce contraseña: ")
contador = 0
for i in range(len(contra)):
  if contra[i] == " ":
    contador = 1
if len(contra)<8 or contador > 0:
  print("Contraseña errónea")
else:
  print("Contraseña correcta")
