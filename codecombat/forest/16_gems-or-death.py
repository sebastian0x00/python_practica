# El código de sentencia if sólo funciona cunado la condición es vedadera. 
# Arregla la sentencia if para superar el nivel.

# == significa "es igual a"
if 1 + 1 + 1 == 4:  # ∆ Haz que esto sea falso
    hero.moveXY(5, 15)  # Muévete a las primeras minas

if 2 + 2 == 4:  # ∆ Haz que esto sea verdadero
	hero.moveXY(15, 40)  # Muévete a la primera gema

# != significa "no es igual a"
if 2 + 2 != 5:  # ∆ Haz que esto sea verdadero
	hero.moveXY(25, 15)  # Muévete a la segunda gema
	
# < significa "es menos que"
if 2 + 2 < 5:  # ∆ Haz que esto sea verdadero
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

if 2  + 3 < 4:  # ∆ Haz que esto sea falso
	hero.moveXY(40, 55)

if False:  # ∆ Haz que esto sea falso
	hero.moveXY(50, 10)

if True:  # ∆ Haz que esto sea verdadero
	hero.moveXY(55, 25)
