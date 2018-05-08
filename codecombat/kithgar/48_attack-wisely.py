# Si caminas sobre una mina, volarás por los aires
hero.moveUp()
hero.moveRight()
hero.moveRight()
hero.moveUp()
hero.moveRight(5)
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
# Aviso 1: Cuanto más grandes, más fuertes
# Aviso 2: No debes matar a todos los ogros si crees que no eres lo suficientemente fuerte
# Abre la puerta usando el comando de ataque sobre('NombredelaPuerta')
hero.moveUp(3)
hero.moveLeft()
hero.moveDown(3)
hero.moveLeft(2)
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(2)
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveDown(2)
hero.moveLeft(2)
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(2)
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveDown(3)
hero.moveLeft(2)
hero.moveUp()
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveUp(2)
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)
    enemy = hero.findNearestEnemy()
hero.moveDown(3)
hero.moveRight(2)
hero.moveDown()





# Ahora vamos a escapar (muévete a la x)
