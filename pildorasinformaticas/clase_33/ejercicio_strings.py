# Ejercicio 1:
# Crea un programa que pida introduciruna dirreción de email por teclado.
# El programa debe imprimir en consola si la dirreción de email es correcta o no en función de si esta tiene un símbolo '@'.
# Si tiene una '@' la dirreción será correcta. Si tiene más de una o ninguna '@' la dirreción será errónea.
# Si la '@' está al comiendo de la dirreción de email o al final, la dirreción también será errónea.

mailUsuario = input("Introduce dirreción de email: ")
arroba = mailUsuario.count('@')

if (arroba!=1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@') == 0):
	print("Mail incorrecto")

else:
	print("Mail correcto")
