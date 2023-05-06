"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
●	Nr secret e mai mare
●	Nr secret e mai mic
●	Felicitări! Ai ghicit!

"""
import random

numar_secret = random.randint(1, 30)
# print(numar_secret)
numar_ghicit = None

while numar_ghicit != numar_secret:
    numar_ghicit = input("Alege un numar de la 1 la 30: ")
    # numar_ghicit = int(numar_ghicit)
    try:
        numar_ghicit = int(numar_ghicit)
    except ValueError:
        print("Nu ai introdus un numar")
        continue

    if numar_ghicit > numar_secret:
        print("Numarul este mai mic")
    else:
        print("Numarul este mai mare")
else:
    print("Felicitari, ai ghicit numarul")
