#Crea un programa que pida dos números por teclado. El programa tendra una funcion llamada "DevuelveMax" encargada de devolver el número más alto de los introducidos

num1 = (int(input("Introduce el primero número: ")))

num2 = (int(input("Introduce el segundo número: ")))

def DevuelveMax (n1, n2):
    if n1 < n2:
        print (n2)
    elif n2 < n1:
        print (n1)
    else:
        print("Son Iguales")

print("El npumero más alto es: ")

DevuelveMax(num1, num2)
