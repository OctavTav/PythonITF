"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
●	Iterează prin ea.
●	Afișează de câte ori apare 3 (nu ai voie să folosești count).

8. Aceeași listă:
●	Iterează prin ea
●	Calculează și afișează suma numerelor (nu ai voie să folosești sum).

9. Aceeași listă:
●	Iterează prin ea.
●	Afișază cel mai mare număr (nu ai voie să folosești max).

10. Aceeași listă:
●	Iterează prin ea.
●	Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
●	Afișază noua listă.

"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)

# for numar in numere:
#     pass
counter = 0
for numar in numere:
    if numar == 3:
        counter += 1
print(f"Numarul 3 apare de {counter} ori")

print('-' * 40)

nr_sum = 0
for numar in numere:
    nr_sum += numar
print(f"Suma numerelor din lista este egala cu {nr_sum}")

print('-' * 40)

nr_max = numere[0]
for numar in numere:
    if nr_max < numar:
        nr_max = numar
print(f"Numarul maxim din lista este {nr_max}")

print('-' * 40)

for i in range(len(numere)):
    if numere[i] > 0 and numere[i] != 0:
        numere[i] = 0 - numere[i]
print(numere)
