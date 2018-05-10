# Write an event handler function called onHear

# Complete the onHear function
def onHear(event):
    # The pet should say something in onHear.
    pet.say("Salutations.")
    pet.say("OK.")
    pet.say("Está bien.")
    pass

pet.on("hear", onHear)

hero.say("Do you understand me?")
hero.say("Are you a cougar?")
hero.say("How old are you?")
# Ask two more questions.
hero.say("Whatsappp?")
hero.say("¿Qué ondaaaa?")
