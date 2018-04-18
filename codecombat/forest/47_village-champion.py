# Incoming munchkins! Defend the town!

# Define your own function to fight the enemy!
def findAndCleaveEnemy():
    # Find the nearest enemy:
    enemy = hero.findNearestEnemy()
    # If an enemy exists:
    if enemy:
        # And if "cleave" is ready:
        if hero.isReady("cleave"):
            # It's time to cleave!
            hero.cleave(enemy)
    pass

def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    pass


# Move between patrol points and call the function.
while True:
    hero.moveXY(35, 34)
    # Use cleaveOrAttack function you defined above.
    findAndCleaveEnemy()
    findAndAttackEnemy()
    hero.moveXY(47, 27)
    # Call the function again.
    findAndCleaveEnemy()
    findAndAttackEnemy()
    hero.moveXY(60, 31)
    # Call the function again.
    findAndCleaveEnemy()
    findAndAttackEnemy()
