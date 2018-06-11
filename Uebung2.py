liste = []
eingabe = ""
i = 0

while(eingabe != "-1"):
    eingabe = input("Bitte eine Zahl eingeben: ")
    zahl = int(eingabe)
    liste.append(zahl)
    liste.remove(-1)

print ("ende.") 

liste.sort()
print(liste)
