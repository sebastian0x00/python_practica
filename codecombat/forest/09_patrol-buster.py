# Recuerda que el enemigo puede no existir todavía.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Si hay un enemigo, ¡atácale!
        hero.attack(enemy)
        pass
