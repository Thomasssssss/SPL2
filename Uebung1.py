zahl1 = input("Bitte 1. Zahl eingeben")
zahl2 = input("Bitte 2. Zahl eingeben")
zahl3 = input("Bitte 3. Zahl eingeben")

if(zahl1 < zahl2 < zahl3):
    print(zahl1,zahl2,zahl3)

if(zahl1 < zahl3 < zahl2):
    print(zahl1,zahl3,zahl2)

if(zahl2 < zahl1 < zahl3):
    print(zahl2,zahl1,zahl3)

if(zahl2 < zahl3 < zahl1):
    print(zahl2,zahl3,zahl1)

if(zahl3 < zahl1 < zahl2):
    print(zahl3,zahl1,zahl2)

if(zahl3 < zahl2 < zahl1):
    print(zahl3,zahl2,zahl1)