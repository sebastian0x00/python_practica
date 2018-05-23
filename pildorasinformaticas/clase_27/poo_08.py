class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 250
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return "El coche está en marcha"

        else:
            return "El coche está parado"


    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un acho de ", self.__anchoChasis, " y un largo de ",
            self.__largoChasis)



miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("---------------A continuación creamos el segundo objeto-------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas = 2

miCoche2.estado()
