import sys

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
    neuer_asciiwert = asciiwert + schlüssel
    # disse funktion wandelt die neue zahl in ein buchstabe um 
    neuer_buchstabe = chr(neuer_asciiwert)
    print("b: %s -> %s [%s -> %s]" % (zeichen, neuer_buchstabe, asciiwert, neuer_asciiwert))
    return neuer_buchstabe
    
    
def verschlüsseln(klartext, schlüssel):
    geheimtext = ""
    
    for buchstabe in klartext:
        neuer_buchstabe = verschieben(buchstabe, True, schlüssel)
        geheimtext = geheimtext + neuer_buchstabe
        print("T: %s" % geheimtext)
        print()
    return geheimtext

def entschlüsseln(geheimtext, schlüssel):
    return geheimtext

def main():
    print("bitte schlüssel eingeben (als zahl): ", end="")
    schlüssel = sys.stdin.readline()
    schlüssel = schlüssel.strip()
    schlüssel = int(schlüssel)
    print("bitte nachricht eingeben: ", end="")
    eingabe = sys.stdin.readline()
    eingabe = eingabe.strip()
    nachricht = verschlüsseln(eingabe, schlüssel)
    print("nachricht: %s" % nachricht)


main()
    
