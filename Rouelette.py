import random
zahlen = []
anzahlWuerfe = input("Wie oft soll Roulette simuliert werden?")
anzahlWuerfe = int(anzahlWuerfe)
for i in range(0,anzahlWuerfe):
    wurf = random.randint(1,36)
    zahlen.append(wurf)

for i in range(1,37):
    print(i,"er : ", zahlen.count(i)) 