# Sobrevive las oleadas de ogros.
# Si ganas, el nivel se hace más difícil, y da mayores recompensas.
# Si pierdes, debes esperar un día para re-enviar.
# Cada vez que envías se generan nuevas condiciones aleatorias.
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
