# ¡Otro cofre en el campo para que el héroe lo abra!
# Ataca el cofre para abrirlo.
# ¡Algunos munchkins no aguantarán mientras tu les atacas!
# Defiéndete cuando un munchkin esté demasiado cerca.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady("cleave"):
        # La primera prioridad es clavar si está listo:
        hero.cleave(enemy)
        pass
    elif distance < 5:
        # Ataca al munchkin más cercano que se te acerque demasiado:
        hero.attack(enemy)
        pass
    else:
        # Si no, prueba a romper el cofre:
        # Use the name of the chest to attack: "Chest".
        hero.attack("Chest")
        pass
    
