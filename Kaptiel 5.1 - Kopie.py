Nachricht = "Hallo" 
Einkaufsliste = ["Milch", "Eier", "Käse", "Sellerie", "Honig"]
print(Einkaufsliste[4])
print("---")
for i in Einkaufsliste:
    print(i)


print("---")
for i in Nachricht:
    print(i)


print("---")
for i in Nachricht:
    print(i.upper())


print("---")
for i in Nachricht:
    x = ord(i)
    print(x)


print("---")
for i in Nachricht:
    x = ord(i) + 13
    print(x)

print("---")
for i in Nachricht:
    x = ord(i) + 13
    print(chr(x))
