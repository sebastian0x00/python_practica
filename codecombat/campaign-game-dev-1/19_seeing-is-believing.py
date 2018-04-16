# Players like seeing score, so use ui.track()!
# It will create a user-interface element for them to see.
hero = game.spawnHeroXY("samurai", 20, 20)

game.addSurviveGoal(20)

spawner = game.spawnXY("generator", 50, 50)
spawner.maxHealth = 9001
spawner.spawnType = "munchkin"
# Add more spawners for more enemies on the field:
spawner2 = game.spawnXY("generator", 50, 50)
spawner2.maxHealth = 9001
spawner2.spawnType = "munchkin"

# ui.track() displays an object's property for players to see!
ui.track(game, "time")
# Use ui.track to track game's "defeated" property:
ui.track(game, "defeated")
hero.attackDamage = 100
# Increase the hero's maxSpeed:
hero.maxSpeed = 50
# Press play and defeat 6 munchkins or skeletons!
