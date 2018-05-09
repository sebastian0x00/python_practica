# La mascota debe saludar al héroe y al campesino.

# Usa esta función como un controlador para eventos "hear":
def sayHello(event):
    # La mascota dice hola:
    pet.say("Saludos.")

# Usa el procedimiento pet's.on("eventType", functionName).
# En este nivel la mascota debe usar sayHello cuando "hear" algo.
pet.on("hear", sayHello)

# Luego saluda a la mascota y espera una respuesta
hero.say("¡Hola, amigo!")
