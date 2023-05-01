"""
Tipuri de date:

1. Numere   -> int (numere intregi)
            -> float (numere cu virgula)
2. Boolean  -> True/False (valoare logica)
3. Siruri de caractere -> string

"""

age = 30        # int
height = 1.78   # float
is_married = False      # boolean
has_children = False    # boolean
first_name = "Octavian" # string
last_name = "Mihaila"   # string
description = "Putem scrie aici orice ne dorim, un string contine cam orice"

alfa = '1234'   # acesta este un String, chiar daca are valoare de numar
beta = 'True'   # tot String
gamma = '1.21'  # tot String


"""
Functia type ne poate zice ce tip de data avem intr-o anumita variabile

"""
print(type(age))
print(type(height))
print(type(is_married))
print(type(first_name))
print('_'*80)
print(type(alfa))
print(type(beta))
print(type(gamma))

"""
Ca sa schimbam tipul unei variabile folosim o tehnica numita type casting
adica avem niste functii speciale (numite int, str, bool, float)

"""
alfa = int(alfa) # as putea folosi si float aici daca as vrea sa obtin un numar zecimal
print('Dupa type casting: ', type(alfa))
beta = bool(beta)
print('Dupa type casting: ', type(beta))
gamma = float(gamma)
print('Dupa type casting: ', type(gamma))

var_x = 'Text care nu poate fi convertit'
# var_x = int(var_x) # Eroare

"""
Int si float pot fi convertite una la cealalta si vice versa
3.14 -> 3
3 -> 3.0

Int si bool pot fi convertite una la cealalta si invers
True -> 1
False -> 0

0 -> False
orice diferite de 0 -> True

Toate tipuri de date se pot converti la String
"""