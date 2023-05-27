"""
class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același
    obiect:
-	Vom folosi functia `__new__` (adevăratul constructor din Python)
-	Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
-	La orice alta apelare, vom returna obiectul deja existent

"""


class PresedinteRomania:
    __obiect_presedinte = None  # facem variabila privata ca sa nu poate fi modificata in afara clasei

    def __new__(cls, *positionalarguments, **keywordarguments):
        if cls.__obiect_presedinte is None:
            cls.__obiect_presedinte = object.__new__(cls)
        return cls.__obiect_presedinte

    def __init__(self, nume):
        self.nume = nume

    def say_hello(self):
        return f'Salut! Eu sunt {self.nume}. Presedintele tau!'


p1 = PresedinteRomania("Taurete")
print(p1.say_hello())

p2 = PresedinteRomania("Gicu Pedala")
print(p2.say_hello())

print(p1.say_hello())

print(id(p1))
print(id(p2))

# class PresedinteRomania:
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def say_hello(self):
#         return f'Salut! {self}'
#
#
# a = PresedinteRomania()
# b = PresedinteRomania()
#
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')
