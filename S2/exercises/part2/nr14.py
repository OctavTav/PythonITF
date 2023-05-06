"""
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333

"""

numar = input("Introdu un numar: ")
numar = int(numar)

for i in range(numar+1):
    for j in range(i):
        print(i, end=" ")
    print()

i = 1
while i <= numar:
    for j in range(i):
        print(i, end=" ")
    print()
    i += 1

for i in range(numar+1):
    print((str(i)+" ")*i)
