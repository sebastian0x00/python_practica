while True:
    # Comprueba la distancia con enemigo más cercano
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # Si estas a 10 metros ,desenfundar .
    if distance < 10:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
    # De lo contrario, atacar el "Cofre"
    else:
        hero.attack("Chest")
    pass
