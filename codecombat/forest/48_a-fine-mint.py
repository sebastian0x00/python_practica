# ¡Los peones tratan de robarte tus monedas!
# Escribe una función para acabar con ellos antes de que puedan robarte las monedas

def pickUpCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

# Escribe la función attackEnemy a continuación:
# Encuentra al enemigo más cercano, ¡y atácalo si lo hay!
def attackenemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    #attackEnemy() # ∆ No rellenes esta línea después de escribir una función attackEnemy.
    attackenemy()
    pickUpCoin()
