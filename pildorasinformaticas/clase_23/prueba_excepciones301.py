
def evaluaedad(edad):

    if edad < 0:
        raise TypeError("No se permite edades negativas")

    if edad < 20:
        return "eres muy joven "
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuídate..."

print(evaluaedad(-15))
