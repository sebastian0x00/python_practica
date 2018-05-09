# Necesitamos conocer el nombre de nuestra nueva mascota

# Use this function as a handler for "hear" events on pet.
def onHear(event):
    # No cambies esta función
    pet.say("Miau Purr Miau")
    pet.say("Purr Purr")
    pet.say("Miau")
    pet.say("Miau")
    pet.say("Miau Purr Miau Miau")

# Usa el pet.on(eventType, eventHandler) métodos
# 
while True:
    pet.on("spawn", onHear)
# Debe ser después de "pet.on"
hero.say("Cómo te llamas, compañero?")
hero.say("Puedes repetírlo?")
