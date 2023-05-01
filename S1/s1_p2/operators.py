"""

Operatori artmetici:

+   adunare
-   scadere
*   inmultire
/   impartire
//  impartire
** ridicare la putere
%   modulo , catul impartirii

"""

a, b = 17, 5
print(a+b)
print(a-b)
print(a*b)

print(a / b)
print(a // b)
print(a % b)

print(a ** 5)

"""
Exista operatori aritmetici care se pot folosi si pe alte tipuri de date:
+(adunare) - se poate folosi si pe string-uri, pentru concatenare
*(inmultire) - se poate folosi pe un string cu un integer si face o concatenare

"""

print ("a" + "b" + "cde")
print("a" * 10)

"""
Operatori de atribuire (asignare)
=(egal) - operator prin care atribuim direct o valoare unei variabile
nume_var op = valoare
"""

x = 5
y = "string"
z = True


x -= 3 # echivalent cu x = x - 3
x += 7 # echivalent cu x = x + 7
x *= 2 # echivalent cu x = x * 2
x **= 3 # echivalent cu x = x ** 3

print(x)
print("_" * 80)

"""
Operatori de comparatie (rezultat va fi mereu boolean , adica  True/False)
== verifica egalitatea
!= verifica inegalitatea
> mai mare
< mai mic
>= mai mare sau egal
<= mai mic sau egal
"""

c, d = 10, 5
print(c == d)
print(c != 5)
print(c > d)
print(c < d)

"""
Operatori  logici ( si, sau, negare ) - functioneaza pe boolean
and - ambele conditii sunt indeplinite
or - cel putin o valoare True
not - schimba valoarea (True devinde False si invers)

"""

age = 17
is_adolescent = age >= 13 and age <= 19

salary = 15000
parents_are_rich = False

person_is_rich = parents_are_rich or salary > 30000

print(not parents_are_rich)