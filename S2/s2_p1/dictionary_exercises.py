from pprint import pprint
"""
Dictionary (dictionar) - o structura de date de tipul cheie - valoare
cu mentiunea ca trebuie sa fie unice

Sintaxa:
{
    cheie1: valaore1,
    cheie2: valoare2,
    ...
    cheieX: valoareX
}
"""

d = {
    'dictionary': 'dictionar',
    'car': 'masina',
    'programming': 'programare'
}

train = {
    'white': 'rocks',
    'red': 'iron',
    'blue': 'cereals',
    # 'white': '' #nu pot avea chei duplicare
    'yellow': 'rocks',
    'pink': 'rocks'
}

"""
Un dictionar se acceseaza la fel ca si o lista, cu diferenta ca aici nu avem indecsi,
asa ca accesam elementele pe baza cheilor
"""

print(train['white']) # va printa 'rocks'
print(train['red'])     # va printa 'iron'

print("-" * 30)

"""
Daca folosim numere intregi incepand cu 0 intr-un dict, este la fel ca si o lista

"""

dict_as_list = {
    0: 'Ana',
    1: 'are',
    2: 'mere'
}
my_list = ['Ana', 'are', 'mere']
print(dict_as_list[0], my_list[0])

print("-" * 30)

"""
In valorile dictionarelor putem pune orice tipuri de date,
dar cheile sunt putin, mai restrictionate:
- putem folosi strings, ints, floats, booleans (toate tipurile)
- NU putem folosi o lista ca si cheie
- NU putem folosi un alt dict ca si cheie
- NU putem folosi un set ca si cheie
- PUTEM folosi o tupla ca si cheie
"""

db = {
    True: "acesta este true",
    False: "acesta este false"
    # True: "" # nu putem repeta cheile
}

dict_complex = {
    'id': 1,
    'name': ['Octavian', 'Mihaila'],
    'height': 1.83,
    'course': {
        'name' : 'Python + Testare automata',
        'start date': '27 Martie 2023'
    }
}
print(dict_complex['name'][0])      # va printa Octavian
print(dict_complex['name'][1])      # va printa Mihaila
print(dict_complex['course']['name'])   # va printa Python + Testare automata

print("-" * 30)

"""
Pentru a afla dimensiunea unui dict folosim len
Dictionarele sunt mutabile (putem adauga, schimba, sterge valori
"""
print(len(dict_complex))

dict_complex['id'] = 10     # schimbarea valorii se face prin atribuirea unei noi valori pe cheie

dict_complex['age'] = 31    # adaugarea unui nou element cheie-valoare
pprint(dict_complex)

del dict_complex['course']  # STERGEREA unui element din dict
pprint(dict_complex)

print("-" * 30)

"""
Putem vedea toate cheile unui dictionar folosind metoda keys()
Putem vedea toate cheile unui dictionar folosind metoda value()
Putem verifica daca o cheie exista intr-un dictionar inainte de a cere valoare acestuia, folosind get()
Putem sterge toate elementele dintr-un dict folosind metoda clear()
"""
print(dict_complex.keys())
# print(dict_complex['course'])   # va da eroare    KeyError: 'course'
print(dict_complex.get('course'))   # va da None, o valoare specifica Python
dict_complex.clear()   # va sterge toate elementele din dictionar
pprint(dict_complex)    # va afisa {}, adica dictionar gol
