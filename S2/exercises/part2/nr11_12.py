"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișează cele 4 liste la final


12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
print(alte_numere)

for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)

    if i >= 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

print('-' * 40)

for i in range(len(alte_numere)):
    for j in range(i, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            c = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = c

print(alte_numere)
