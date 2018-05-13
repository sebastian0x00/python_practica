# Mueve a Lado y lograsu número secreto.
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# Sumario 7 al número de Lado para lograr el número de Erzsebet
# Muévete hasta Erzsebet y di su número mágico.
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)

# Divide el número de Erzsebet entre 4 para lograr el número de Simonyi.
# Vete donde Simonyi y dile su número.
sim = erz / 4
hero.moveXY(30, 39)
hero.say(sim)
# Multiplica el número de Simonyi por el de Laszlo para obtener el número de Agata.
# Vete donde Agata y dile su número.
aga = sim * las
hero.moveXY(43, 27)
hero.say(aga)
