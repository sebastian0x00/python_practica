# ¡Permanece en el centro y defiende!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Ataca al enemigo...
        hero.attack(enemy)
        pass
    else:
        # ... o vuelve a tu posición defensiva.
        hero.moveXY(40, 34)
        pass
