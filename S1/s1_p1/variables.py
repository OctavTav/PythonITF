"""
Variabila  = o locatie din memorie care tine o valoare si are un nume
1. Variabilele au nume unice, pentru ale putea identifica
2. Numele de variabile in python sunt valide daca contin litere mici, mari, numere, underscore
3. In general, numele de variabile in pyhton folosesc litere mici si underscore
4. In general, numele de constante in Python folosesc doar litere mari si underscore
5. Numele de variabile pot incepe cu litere sau underscore, NU cu cifre
6. Numele de variabile sunt case-sensitive
"""

varsta_mea = 24 # nume valid
VARSTA_MEA = 24 # nume valid, nu e bun in Python => este defapt constanta
PI = 3.1415 # nume valid, constanta
VarstaMea = 24 # nume valid, dar nu e bun in Python
print(varsta_mea)
# Varsta mea = 24 # nume invalid, deoarece contine spatiu
_variabila_mea = 24 # nume valid, dar nu e recomandat, are o anumita atributie
# 21variabila = 24 # nu e valid

"""
Putem schimba   valoare variabilelor pe parcursul unui program 
                tipul de data pe care acestea o contin
"""
varsta_mea = 25 # am schimbat valoarea variabilei varsta_mea
print(varsta_mea)


"""
Putem atribui mai multe valori intr-o singura linie 
sau aceeasi valoare mai multor variabile
a, b, c = 10, 20, 30
"""
# a, b, c = 10, 20    #eroare
# a, b, c = 10, 20, 30, 40    #eroare
a, b, c = 10, 20, 30
# Toate cele 3 variabile vor avea valoarea 100, dar sunt variabile diferite
x = y = z = 100