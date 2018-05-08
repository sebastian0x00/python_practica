#Crea un programa que pida por teclado "Nombre", "Dirreción" y "Tfno". Esos tres datos deberan ser almacenados en una lista y mostrar en consola el mensaje: "Los datos persoanles son: nombre apellido y teléfono" (Se mostrarán los datos introducidos por teclado).

Nombre = input("Introduce el nombre: ")

Dirrecion = input("Introduce la dirreción: ")

Tfno = input("Introduce el teléfono: ")

listaDatos = [Nombre, Dirrecion, Tfno]

print("Los datos personales son: " + listaDatos[0] + " " + listaDatos[1] + " " + listaDatos[2])
