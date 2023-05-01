cars = [['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] ]
# ca sa pot modifica lista, am nevoie de indecsii acesteia, asa ca for-ul meu va di pe indecsi

# for idx in range(len(cars)):
#     print(f'{idx}: {cars[idx]}')

# for idx in range(len(cars)):
#     if idx == 0 or idx == len(cars)-1:
#         continue
#     cars[idx] = cars[idx].upper()
# else:
#     print(cars)


pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000

}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Masina {masina} costa {pret} si se incadreaza in buget')
