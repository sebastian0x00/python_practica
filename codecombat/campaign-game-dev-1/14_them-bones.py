# Generators spawn enemies over time.
# Skeletons are afraid of lightstones.

player = game.spawnHeroXY("champion", 15, 35)
player.attackDamage = 60
player.maxSpeed = 8

game.addSurviveGoal()
game.addDefeatGoal()
game.spawnXY("x-mark-stone", 60, 35)
# Spawn a "generator"
game.spawnXY("generator", 49, 18)
# Spawn a "lightstone"
game.spawnXY("lightstone", 41, 32)
game.spawnXY("lightstone", 41, 36)
game.spawnXY("lightstone", 41, 40)
game.spawnXY("lightstone", 41, 42)
# Now beat your game!
