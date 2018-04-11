def divide():

    try:
        op1 = (float(input("Introduce el primer número: ")))

        op2 = (float(input("Introduce el segundo número: ")))

        print("La división es: " + str(op1/op2))

    finally:

        print("Cáculo finalizado")

divide()
