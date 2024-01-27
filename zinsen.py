betrag = 100000
zinsatz = 0.20
jahr = 2026
spar_dauer = 3 

kontostand = betrag

print ("jahr %d: kontostand: %d " % (jahr, kontostand))

for j in range (0, spar_dauer+1):
    x =(kontostand * zinsatz) 
    print (x)
    kontostand = kontostand + x
    jahr = jahr + 1 
    print ("jahr %d: kontostand: %d " % (jahr, kontostand))
