# Puedes introducir una sentencia if dentro de otra sentencia if
# Ten cuidado en como las sentencias if interactuan unas con otras.
# Asegúrate que el tabulado-sangrado es correcto
# Es útil comenzar con un  if / else,
# Use comentarios como marcadores de posición para el if / else:

while True:
    enemy = hero.findNearestEnemy()
    # Si hay un enemigo, entonces...
    if enemy:
        # Cree una variable de distancia con distanceTo.
        distance = hero.distanceTo(enemy)
        # Si la distancia es menor de 5 metros, ataque.
        if distance < 5:
            hero.attack(enemy) 
        # Sino (el enemigo está lejos), pues protégete.
        else:
            if distance > 5:
                hero.shield()
        pass
    # Sino (no hay enemigo)...
    else:
        # ... luego regresa a la posición X
        hero.moveXY(40, 34)
