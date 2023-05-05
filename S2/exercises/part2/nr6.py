"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

●	Prezintă doar mașinile care se încadrează în acest buget.
●	Iterează prin dict.items() și accesează mașina și prețul.
●	Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
●	Iterează prin listă.
"""

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BWM': 23000
}

client_buget = 15000
able_to_buy = False
print(f"In bugetul dumneavoastra de {client_buget} ")
for masina, pret in pret_masini.items():
    if pret <= client_buget:
        print(f"se incadreaza {masina} cu pretul de {pret}")
        able_to_buy = True

if not able_to_buy:
    print("Nu se incadreaza nici o masina")

print(f"Pentru un buget de {client_buget} puteti alege pana la {client_buget/pret_masini['Lastun']:.0f} masini Lastun")

masini = tuple(pret_masini.keys())

print(masini)

print('-' * 40)

masini = tuple(pret_masini)
