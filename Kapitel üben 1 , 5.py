hausarbeit = 5
zeitung = 30
ausgaben = 10
(hausarbeit + zeitung - ausgaben) * 52 
1300

erspartes = 0
for woche in range(1, 53):
    erspartes = erspartes + hausarbeit + zeitung - ausgaben
    print("%s Woche = %s" % (woche, erspartes))
