# Cuando juegues, haz clic en un ogro para atacar!
# No es necesario escribir ningún código para este nivel, simplemente haga clic en Play!

# El siguiente código genera un héroe para jugar:
game.spawnHeroXY("guardian", 40, 40)

# Estos añaden objetivos al nivel:
game.addDefeatGoal()
game.addSurviveGoal()

# Esto genera algunos enemigos para luchar:
game.spawnXY("munchkin", 40, 25)
game.spawnXY("munchkin", 15, 15)
game.spawnXY("munchkin", 65, 15)

# Esto genera un laberinto para el jugador:
game.spawnXY("forest", 30, 54)
game.spawnXY("forest", 50, 54)
game.spawnXY("forest", 30, 48)
game.spawnXY("forest", 50, 48)
game.spawnXY("forest", 30, 40)
game.spawnXY("forest", 50, 40)
game.spawnXY("forest", 30, 32)
game.spawnXY("forest", 50, 32)
game.spawnXY("forest", 30, 26)
game.spawnXY("forest", 50, 26)
game.spawnXY("forest", 30, 10)
game.spawnXY("forest", 50, 10)
game.spawnXY("forest", 22, 26)
game.spawnXY("forest", 58, 26)
game.spawnXY("forest", 14, 26)
game.spawnXY("forest", 66, 26)
