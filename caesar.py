import sys

def verschlüsseln(klartext, schlüssel):
    geheimtext = ""
    
    for buchstabe in klartext:
        asciiwert = ord(buchstabe)
        neuer_asciiwert = asciiwert + schlüssel
        neuer_buchstabe = chr(neuer_asciiwert)
        print("b: %s -> %s [%s -> %s]" % (buchstabe, neuer_buchstabe, asciiwert, neuer_asciiwert))
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
    
