# Recuerda que el enemigo puede no existir todavía.
while True:
    enemy = hero.findNearestEnemy()
    # Si hay un enemigo, ¡atácale!
    if enemy:
        hero.attack(enemy)
        pass    
