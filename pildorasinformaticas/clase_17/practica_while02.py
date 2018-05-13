edad = int(input("Introduce la edad, por favor"))

while edad < 0:
    print("Has introducido una edad negativa. Vuelve a intentarlo")
    edad = int(input("Introduce la edad, por favor"))

print("Gracias por la colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))
