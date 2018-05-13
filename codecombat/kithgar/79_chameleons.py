# ¡Los Ogros están disfrazados de monedas o gemas!

while True:
    enemy = hero.findNearestEnemy()
    # Si tu ves a un enemigo - atacalo:
    if enemy:
        hero.attack(enemy)
    item = hero.findNearestItem()
    # Si tu ves una moneda o una gema - muévete a su posición X y Y
    item = hero.findNearestItem()
    if item:
        pos = item.pos
        X = pos.x
        Y = pos.y
        hero.moveXY(X, Y)
