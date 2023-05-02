"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
●	Adaugă în zilele_sapt ‘luni’
●	Afișează zile_sapt

14.Folosește un if și verifică dacă:
●	Weekend este un subset al zilelor din săptămânii.
●	Weekend nu este un subset al zilelor din săptămânii.

15. Afișează diferențele dintre aceste 2 seturi.

16. Afișează intersecția elementelor din aceste 2 seturi.

"""

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)
print('-' * 40)
if weekend.issubset(zile_sapt):
    print("weekend este un subset al zile_sapt")
else:
    print("weekend nu este un subset al zile_sapt")
print('-' * 40)
print(zile_sapt.difference(weekend))
print('-' * 40)
print(zile_sapt.intersection(weekend))
