while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # Ataca si se acercan mucho al campesino.
        hero.attack(enemy)
        pass
    # Si no, ¡quédate cerca del campesino! Usa else.
    else:
        hero.moveXY(40, 40)
    
