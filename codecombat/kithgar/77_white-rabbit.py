# Follow the lightstone to navigate the traps.

while True:
    item = hero.findNearestItem()
    if item:
        # Store the item's position in a new variable using item.pos:
        pos = item.pos
        # Store the X and Y coordinates using pos.x and pos.y:
        X = pos.x
        Y = pos.y
        # Move to the coordinates using moveXY() and the X and Y variables:
        hero.moveXY(X, Y)
        pass
