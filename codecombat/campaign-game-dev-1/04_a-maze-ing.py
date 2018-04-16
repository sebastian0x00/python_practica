# A Alejandro le gusta el reto!
# Añade más objetos "forest" al nivel para crear un laberinto largo.

# Establecer el objetivo del juego.
game.addCollectGoal()
# Selecciona un héroe y genera cofres para recolectar
game.spawnHeroXY("duelist", 9, 59)
game.spawnXY("chest", 8, 14)

game.spawnXY("forest", 26, 51)
# Añade 2 objetos "forest" mas. Asegúrate de no bloquear las gemas por completo!
mySpawn = game.spawnXY("forest", 49, 34)
mySpawn = game.spawnXY("forest", 75, 7)
