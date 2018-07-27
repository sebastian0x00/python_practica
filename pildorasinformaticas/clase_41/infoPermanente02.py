import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona nueva con el nombre de ", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:

	personas = []

	def agregarPersonas(self, p):
		self.personas.append(p)

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)


miLista = ListaPersonas()
p = Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(p)
p = Persona("Antonio", "Masculino", 39)
miLista.agregarPersonas(p)
p = Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()
