# Cura los sondados aluados para sobrevivir el asedio.
while True:
    if hero.canCast("regen"):
        bernardDistance = hero.distanceTo("Bernard")
        if bernardDistance < 10:
            # ¡Bernard necesita ser regenerado!
            hero.cast("regen", "Bernard")
        
        # Usa "if" y "distanceTo" para regenerar a "Chandra"
        # si está a menos de 10 metros.
        chandraDistance = hero.distanceTo("Chandra")
        if chandraDistance < 10:
            hero.cast("regen", "Chandra")
    else:
        # Si no estás lanzado "regen", usa "if" y "distanceTo".
        # para atacar enemigos que están más cerca de  hero.attackRange.
        enemy = hero.findNearestEnemy()
        if enemy and hero.distanceTo(enemy) < hero.attackRange:
            hero.attack(enemy)
        pass
