# Desplázate a todas las marcas X
# Estas minas explosivas hacen daño!

game.spawnHeroXY("samurai", 40, 50)
game.addSurviveGoal()
game.addMoveGoalXY(25,40)
game.spawnXY("fire-trap", 25, 40)
game.addMoveGoalXY(55,40)
game.spawnXY("fire-trap", 55, 40)
game.addMoveGoalXY(40,20)
game.spawnXY("fire-trap", 40, 20)

# Genera algunas "pociones pequeñas" "potion-small" para sanar al jugador!
game.spawnXY("potion-small", 25, 20)
game.spawnXY("potion-small", 20, 20)
game.spawnXY("potion-small", 15, 30)
game.spawnXY("potion-small", 10, 20)
