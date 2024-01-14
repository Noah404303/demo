def meine_funktion(vorname,nachname):
    print("Hallo %s %s" % (nachname,vorname))

meine_funktion("Noah", "Mikolajewski")
meine_funktion("Daniel", "Esther")




def ersparnisse(hausarbeit, zeitung, ausgaben):
    return hausarbeit + zeitung - ausgaben

x = ersparnisse(10, 10, 5)
print("Hallo das sind die Ersparnisse: %s " % x )



def GlücksZahl():
    return 42

def Lottospiel(Zahl):
    print("Lotto: %s " % Zahl ) 

g = GlücksZahl()
Lottospiel(g)

def umdrehen(text):
    return text[::-1]

def Verschlüsseln(Klartext):
    return umdrehen(Klartext)

def Entschlüsseln(Geheimtext):
    return Geheimtext[::-1]

nachricht = Verschlüsseln("das ist geheim")
print("nachricht:%s" % nachricht)
empfangen_nachircht = Entschlüsseln(nachricht)
print("empfangen: %s" % empfangen_nachircht)
