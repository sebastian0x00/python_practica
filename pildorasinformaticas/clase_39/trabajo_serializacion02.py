#para leer en binario

import pickle

fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

print(lista)
