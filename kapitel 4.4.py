spieler1 = 100
spieler2 = 300
spieler3 = 500
if spieler1 is None or spieler2 is None or spieler3 is None:
    print("warte bitte bis alle Spieler zurückgekommen sind")
else:
    print("Ihr habt %s gesammelt" % (spieler1 + spieler2 + spieler3))
