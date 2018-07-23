from io import open

archivo_texto = open("archivo.txt", "r+") #lectura y escritura

# print(archivo_texto.readlines()) #para comprobar las lineas, muestra 3, separadas por \n

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta línea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
