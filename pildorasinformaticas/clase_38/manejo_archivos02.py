from io import open

archivo_texto = open("archivo.txt", "r")

#archivo_texto.seek(11)

print(archivo_texto.read(11))

print(archivo_texto.read())
