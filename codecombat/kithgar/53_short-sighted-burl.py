# Collect coins and run lest the burl will find you.

# The function allows your hero take an item.
def takeItem(item):
    hero.moveXY(item.pos.x, item.pos.y)

# Write the function "checkTakeRun" with one parameter.
# If the item exists, use "takeItem" function to take it.
# Move to the start point (the green mark) whether the item or no.
def checkTakeRun(target):
    if target:
        takeItem(target)
        hero.moveXY(40, 12)
    else:
        hero.moveXY(40, 12)

# Don't change this code.
while True:
    hero.moveXY(16, 56)
    coin = hero.findNearestItem()
    checkTakeRun(coin)
    hero.moveXY(64, 56)
    coin = hero.findNearestItem()
    checkTakeRun(coin)
