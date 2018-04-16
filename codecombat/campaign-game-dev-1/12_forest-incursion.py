# Okar needs to stomp out these annoying little munchkins!
# Unfortunately he is slow, and his attacks do little damage.
# Fortunately, as a game developer, you have full control over the world!
# Set Okar's properties to buff him up for ogre slaying!
# You can find default values for units on the doc panel.

game.addDefeatGoal()
game.addSurviveGoal()
hero = game.spawnHeroXY("goliath", 12, 10)
# Increase the hero's maxSpeed ( > 4), so he runs faster.
hero.maxSpeed = 25
# Increase the hero's maxHealth ( > 500), so he lasts longer.
hero.maxHealth = 750
# Increase the hero's attackDamage ( > 7.68), so he can quickly take down the ogres.
hero.attackDamage = 9001
