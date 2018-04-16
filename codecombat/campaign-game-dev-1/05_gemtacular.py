# Anya está buscando gemas!
# Añade gemas al nivel para que el jugador las busque!
# Debes ser capaz de completar tu propio nivel creado para continuar

game.spawnHeroXY("captain", 9, 18)
# Añade un objetivo de coleccionar gemas usando el comando game.addCollectGoal()
game.addCollectGoal()
game.spawnXY("gem", 28, 28)
# Añade 3 gemas más sobre el nivel para que el jugador las recoja:
game.spawnXY("gem", 11, 10)
game.spawnXY("gem", 44, 10)
game.spawnXY("gem", 46, 26)
