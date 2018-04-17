# ¡Navega a través de los bosques, pero permanece alerta!
# ¡Esos bosques con forma de cubo pueden tener ogros!

hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# La sentencia if verificará si la variable tiene un ogro.
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(49, 51)
enemy = hero.findNearestEnemy()
if enemy:
    # Ataca al enemigo aquí.
    hero.attack(enemy)
    hero.attack(enemy)
    
    # pass no significa nada. Ayuda a para saber donde se cierra la sentencia if
    pass

hero.moveXY(58, 14)
enemy = hero.findNearestEnemy()
# Usa una sentencia if para verificar si el enemigo existe.
if enemy:
    # Si el enemigo existe, atácalo.
    hero.attack(enemy)
    hero.attack(enemy)
    pass
    
