def cleaveOrAttack(enemy):
    # If "cleave" is ready, cleave; otherwise, attack.
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            # Call the "cleaveOrAttack" function, defined above.
            cleaveOrAttack(enemy)
