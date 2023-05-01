"""
While - bucla (loop) iterativa in care un cod se executa CAT TIMP
o anumita conditie este adevarata

while( <conditie>:
    fa ceva
    fa altceva
    samd
"""

"""
Presupunem ca utilizatorul va introduce varsta corecta (adica un numar) -> True
Daca varsta este corecta dam break la bucla
"""
while True:
    age = input("Introdu varsta: ")
    if age.isdigit():
        break
print(f'Varsta este {int(age)}')

"""
Cerem input de la utilizator
CAT TIMP utilizatorul NU introduce varsta, se continua WHILE
"""

varsta = input("Introdu varsta: ")
while not varsta.isdigit():
    varsta = input("Introdu varsta: ")
print(f'Inaltime de {varsta}')