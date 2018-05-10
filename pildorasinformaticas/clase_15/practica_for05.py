email=False

for i in "juan@pildorasinformaticas.es":
	if(i=="@"):
		email=True

if email==True:
	print("Email es correcto")
else:
	print("El email no es correcto")
