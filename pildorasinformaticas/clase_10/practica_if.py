def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(4))
