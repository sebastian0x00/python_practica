class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre = nombre

		self.edad = edad

		self.lugar_residencia = Lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antiguedad):

		super().__init__("Antonio", 55, "España")

		self.salario = salario

		self.antiguedad = antiguedad


Antonio = Empleado(1500, 15)

Antonio.descripcion()
