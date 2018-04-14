# Usa un loop para atacar el esqueleto.
# Su desafilada arma apenas crea daños pero tiene un tremendo mandoble
enemy = hero.findNearestEnemy()

while True:
    hero.attack(enemy)
