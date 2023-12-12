def jahres_ersparnisse(hausarbeit, zeitung, ausgaben):
    ersparnisse = 0
    for woche in range(1, 53):
        ersparnisse = ersparnisse + hausarbeit + zeitung - ausgaben
        print("Woche %s = %s" % (woche, ersparnisse))
jahres_ersparnisse(10, 10, 5)
jahres_ersparnisse(25, 15 , 10)

