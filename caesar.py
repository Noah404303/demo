import sys

def ist_kleiner_buchstabe(asciiwert):
    # überprüfung ob zeichen in asciitabele zwischen a und z ist
    # a : 97
    # z : 122
    if asciiwert >= 97 and asciiwert <= 122:
        return True
    else:
        return False
    
# diese funktion rutiert die zeichen fals ans ende des Alphapet kommt
# berechnung:
#
# z = 122 wenn es um 1 verschoben wird hatt es den wer 123 und es ist nicht mehr in Alphapet.
# wir wollen das daraus ein a wird mit denn wert 97
#
# die rechnung für die rutation von z :
# 97 = 123 - x
#
# 97 = 123 - x | +x
# 97 + x = 123 | -97
# x = 123 - 97
# x = 26
#
# überaschung: 26 ist die anzahl der zeichen in Alphabet
# das bedeutet wir konnen immer wen wir Alphabet hinaus gehen für jedes zeiuchen die rutationen in demm wir - 26 rechnen vom werschobenen asciiwert.
# beistpiel:
#
# Schlüssel: 13, buchstabe: T (asciiwert: 84)
# manuel rutation: 84 + 13 = 97
# 97 ist größer alls Z (90) druch händisches zehlen kommt man auf den wer G (71)
#
# 97-26 = 71
#
# pseudo code :
# festellen ob großer oder kleiner buchstabe
# wenn Kleiner buchstabe dann überprüfen ob <= z (122), dann keine Rotation vor nehmen . asciiwert un verändert züruck geben.
# wenn großer buchstabe dann überprüfen ob <= Z (90), dann keine Rotation vor nehmen . asciiwert un verändert züruck geben.
# ansonsten: asciiwert - 26 züruck geben
def rotieren(original_asciiwert, asciiwert):
    # kleiner buchstabe
    if ist_kleiner_buchstabe(original_asciiwert):
        # kleiner alls z kein rotiren notwendig 
        if asciiwert <= 122:
            return asciiwert
    # Großer buchstabe 
    else:
        # kleiner alls Z kein rotiren notwendig 
        if asciiwert <= 90:
            return asciiwert

    # ansonsten: wir müssen rotieren 
    return asciiwert - 26 

def rotieren_rückwärts(original_asciiwert, asciiwert):
    # kleiner buchstabe
    if ist_kleiner_buchstabe(original_asciiwert):
        # Größer gleich a kein rotiren notwendig 
        if asciiwert >= 97:
            return asciiwert
    # Großer buchstabe 
    else:
        # Größer gleich A kein rotiren notwendig 
        if asciiwert >= 65:
            return asciiwert

    # ansonsten: wir müssen rotieren 
    return asciiwert + 26 


# dise funktion nimt eine asciizahl und überpruft ob es sich um ein buchstabe von alphabet handelt 
def im_alphabet(asciiwert):
    # überprüfung ob zeichen in asciitabele zwischen A und Z ist
    # A : 65
    # Z : 90
    if asciiwert >= 65 and asciiwert <= 90:
        return True

    # überprüfung ob zeichen in asciitabele zwischen a und z ist
    # a : 97
    # z : 122
    elif asciiwert >= 97 and asciiwert <= 122:
        return True
    else:
        return False

# disse funktion verschibt nur zeichen von alphabet die keine sonder zeichen sind
# die verschiebung ist abhengig vom schlüssel wert 
def verschieben(zeichen, vorwärts, schlüssel):
    # die ord funktion wandeld ein zeichen in ein asciizahl um. später wir mit der funktion "chr" züruck um gewandelt 
    asciiwert = ord(zeichen)
    if im_alphabet(asciiwert) == False:
        return zeichen

    # hier findet die eigentliche verschibung stad und das passirt durch + rechnung mit asciizahl und schlüssel zahl
    if vorwärts:
        neuer_asciiwert = asciiwert + schlüssel
        # rotiren falls notwenig
        neuer_asciiwert = rotieren(asciiwert, neuer_asciiwert)
    else:
        neuer_asciiwert = asciiwert - schlüssel
        # rotiren_rückwerts falls notwenig
        neuer_asciiwert = rotieren_rückwärts(asciiwert, neuer_asciiwert)
    
    # disse funktion wandelt die neue zahl in ein buchstabe um 
    neuer_buchstabe = chr(neuer_asciiwert)
    # print("b: %s -> %s [%s -> %s]" % (zeichen, neuer_buchstabe, asciiwert, neuer_asciiwert))
    return neuer_buchstabe
    
    
def verschlüsseln(klartext, schlüssel):
    geheimtext = ""
    
    for buchstabe in klartext:
        neuer_buchstabe = verschieben(buchstabe, True, schlüssel)
        geheimtext = geheimtext + neuer_buchstabe
        # print("T: %s" % geheimtext)
        # print()
    return geheimtext

def entschlüsseln(geheimtext, schlüssel):
    klartext = ""
    for buchstabe in geheimtext:
        neuer_buchstabe = verschieben(buchstabe, False, schlüssel)
        klartext = klartext + neuer_buchstabe
        # print("T: %s" % klartext)
        # print()

    return klartext 

def main():
    print("bitte schlüssel eingeben (als zahl): ", end="")
    schlüssel = sys.stdin.readline()
    schlüssel = schlüssel.strip()
    schlüssel = int(schlüssel)
    print("bitte nachricht eingeben: ", end="")
    eingabe = sys.stdin.readline()
    eingabe = eingabe.strip()
    verschlüsselte_nachricht = verschlüsseln(eingabe, schlüssel)
    print("verschlüsselte nachricht: %s" % verschlüsselte_nachricht)



    entschlüsselte_nachricht = entschlüsseln(verschlüsselte_nachricht, schlüssel)
    print("entschlüsselte nachricht: %s" % entschlüsselte_nachricht)


main()
    
