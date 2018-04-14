hero.moveRight()

# Deberías acordarte de esto del último nivel.
enemy1 = hero.findNearestEnemy()
# Ahora atacar a enemy1
hero.attack(enemy1)
hero.attack(enemy1)
hero.moveRight(2)
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.moveRight()
