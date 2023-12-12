betrag = 100
zinsatz = 0.03
jahr = 2023
spar_dauer = 10

kontostand = betrag

print ("jahr %d: kontostand: %d " % (jahr, kontostand))

for j in range (0, spar_dauer+1):
    x =(kontostand * zinsatz) 
    print (x)
    kontostand = kontostand + x
    jahr = jahr + 1 
    print ("jahr %d: kontostand: %d " % (jahr, kontostand))
