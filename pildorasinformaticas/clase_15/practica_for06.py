contador = 0
miEmail=input("Introduce tu dirreción de email: ")

for i in miEmail:
	if(i=="@" or i=="."):
		contador=contador+1


if contador==2:
	print("Email es correcto")
else:
	print("El email no es correcto")
