"""
Set - structura de date care nu permite duplicate
- NU sunt ordonate si NICI indexate, putem doar adauga sau sterge elemente

Sintaxa:
{elem1, elem2, elem3,..., elemX}
"""

s = {1, 2, 3, 1}
print(s)        # va printa {1, 2, 3}, deoarece setul nu permite duplicate

s.add(7)
s.add(3)        # va printa {1, 2, 3, 7}

s.remove(2)     # vom scoate elem cu valoare 2

"""
Si setul poate tine aproape orice tipuri de date
- toate tipurile basic (int, float, bool, string)
- liste NU
- dictionare NU
- alte seturi NU
- tuple DA
Practic, setul poate avea doar valori imutabile, adica nu pot fi modificate
"""

set_complex = {1, 2, True, False, 'Ana are mere'}
print(set_complex)

# set_gol = {}      # nu putem face asa, este dictionar
set_gol = set()     # asa facem un set gol
set_gol.add(12)
set_gol.add(True)
set_gol.add("stringulet")
print(set_gol)
set_gol.clear()     # stergem toate elem din set

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.intersection(b))    # printeaza elem comune
print(a.difference(b))      # printeaza elem existente doar in a
print(b.difference(a))      # printeaza elem existene DOAR in b
print(a.union(b))           # printeaza  suma elem  din cele 2
