# Usa un bucle while-true para moverte y atacar.

while True:
    hero.moveRight()
    hero.moveUp()
    hero.moveRight()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveDown(2)
    hero.moveUp()    
    pass
