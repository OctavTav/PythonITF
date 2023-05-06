"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
●	‘Mașina mea preferată este x’.
●	Fă același lucru cu un for each.
●	Fă același lucru cu un while.

2. Aceeași listă:
Folosește un for else
În for
-	Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
-	  Printează lista.


3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘


4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.

-	Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
-	Printează S-ar putea să vă placă mașina x.

5. Modernizează parcul de mașini:

●	Crează o listă goală, masini_vechi.
●	Iterează prin mașini.
●	Când găsesti Lăstun sau Trabant:
-	Salvează aceste mașini în masini_vechi.
-	Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
●	Printează Modele vechi: x.
●	Modele noi: x.

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    print(f"Masina mea preferata este {masini[x]}")
print()
for x in masini:
    print(f"Masina mea preferata este {x}")
print()
x = 0
while x < len(masini):
    print(f"Masina mea preferata este {masini[x]}")
    x += 1

print('-' * 40)

for x in range(len(masini)):
    if x != 0 and x != len(masini)-1:
        masini[x] = masini[x].upper()
else:
    print(masini)

print('-' * 40)

for x in masini:
    if x.capitalize() == 'Mercedes':
        print("Am gasit masina dorita de dvs")
        break
    else:
        print(f"Am gasit masina {x}, mai cautam")

print('-' * 40)

for x in masini:
    if x.capitalize() == 'Trabant' or x.capitalize() == 'Lastun':
        continue
    else:
        print(f"S-ar putea sa va placa masina {x}")

print('-' * 40)

masini_vechi = []
# for x in range(len(masini)):
#     if masini[x].capitalize() == 'Lastun' or masini[x].capitalize() == 'Trabant':
#         masini_vechi.append(masini[x])
#         masini[x] = 'Tesla'

for x in masini:
    if x.capitalize() == 'Lastun' or x.capitalize() == 'Trabant':
        masini_vechi.append(x)
        pos = masini.index(x)
        masini[pos] = masini[pos].replace(x, 'Tesla')

print(f"Modele vechi {masini_vechi}")
print(f"Modele noi {masini}")
