hero.moveDown()

# Mamá siempre ha dicho que nos comamos las setas que encontremos en los calabozos.
hero.moveRight()
hero.moveDown()
hero.moveDown()
hero.moveRight()
hero.moveRight()
hero.moveRight()
hero.moveUp()
hero.moveLeft()
hero.moveUp()
hero.moveRight()
hero.moveUp()
hero.moveLeft()
hero.moveDown()

# Encuentra el camino que te guíe hacia el guardián.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
