# Comprueba si las minas son seguras para los trabajadores.

def checkEnemyOrSafe(target):
    # Si el objetivo (el parámetro) existe:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Luego ataca al objetivo.
        hero.attack(enemy)
    # De otra manera:
    else:
        # Usa say() para llamar a los campesinos.
        hero.say("peasants")
    pass

while True:
    # Muévete hasta la marca X superior derecha y verifícala.
    hero.moveXY(64, 54)
    enemy1 = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy1)
    
    # Muévete a la marca X inferior izquierda.
    hero.moveXY(16, 14)
    # Guarda el resultado de findNearestEnemy () en una variable.
    enemy2 = hero.findNearestEnemy();
    # Llámalo checkEnemyOrSafe, y pasa el 
    # resultado de findNearestEnemy como argumento.
    checkEnemyOrSafe()
    pass
