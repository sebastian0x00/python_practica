class Coche():
    #propiedades del tipo de coche
    largoChasis = 250
    anchoChasis = 250
    ruedas = 4
    enmarcha = False

    def arrancar(self):   #comportamiento, arrancar es el metodo
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"

        else:
            return "El coche está parado"

miCoche = Coche() #instanciar una clase

print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, "ruedas")
miCoche.arrancar()

print(miCoche.estado())

print("---------------A continuación creamos el segundo objeto-------------")

miCoche2 =  Coche()

print("El largo del coche es: ", miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas, "ruedas")
print(miCoche2.estado())
