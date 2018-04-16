# Todo juego debe tener un héroe y una meta

# Usa game.spawnHeroXY ("captain", x, y) para añadir un héroe al juego:
# to add a hero to your game:
game.spawnHeroXY("captain", 36, 30)
# Utilice game.addMoveGoalXY (x, y) para agregar una meta de destino
# to add a movement goal to your game:
# it should be 10m away from the hero.
game.addMoveGoalXY(40, 10)
# Si quieres, use spawnXY ("fence", x, y) para hacer un laberinto con vallas ...
# to make a maze with fences...
mySpawn = game.spawnXY("fence", 15, 23)
# A continuación, haga clic en "Play" para probar su primer juego editado!
