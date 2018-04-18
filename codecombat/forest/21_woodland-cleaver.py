# Usa tu nueva habilidad "cleave" tan a menudo como puedas

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        # ¡Ahuyenta al enemigo!
        hero.cleave(enemy)
        pass
    else:
        # Si no (si cleave no está listo), haz un ataque normal.
        hero.attack(enemy)
        pass
