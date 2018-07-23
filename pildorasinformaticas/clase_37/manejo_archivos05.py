from io import open

archivo_texto = open("archivo.txt", "a") #append (agregar, extension)

archivo_texto.write("\n siempre es una buena ocación para estudiar Python")

archivo_texto.close()
