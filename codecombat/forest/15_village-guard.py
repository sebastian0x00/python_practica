# Patrulla las entradas de la aldea.
# Su encuentras un enemigo, atácalo.
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    # Ahora muévete a la entrada de la derecha
    hero.moveXY(60, 31)
    # Encuentra al enemigo de la derecha.
    derecha = hero.findNearestEnemy()
    # Usa "if"para atacar si hay un enemigo de la derecha
    if derecha:
        hero.attack(derecha)
        hero.attack(derecha)
