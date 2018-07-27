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

	def __init__(self):

		listaDePersonas = open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas = pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		
		except:
			print("El fichero está vacío")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)


miLista = ListaPersonas()
