def enemyInRange(enemy):
    # Devuelve "True" si el enemigo está más cerca que 5 unidades.
    distance = hero.distanceTo(enemy)
    if distance < 5:
        return True
    else:
        return False

def cleaveOrAttack(enemy):
    if hero.isReady('cleave'):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Comprueba la distancia con el enemigo usando la función enemyInRange.
        if enemyInRange(enemy):
            cleaveOrAttack(enemy)
