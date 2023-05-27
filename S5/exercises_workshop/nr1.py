"""
1.	Singleton
Se da următoarea clasa:


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
Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
-	Vom folosi functia `__new__` (adevăratul constructor din Python)
-	Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
-	La orice alta apelare, vom returna obiectul deja existent
"""


"""class PresedinteRomania:
    __instance = None

    @staticmethod
    def get_instance():
        if PresedinteRomania.__instance is None:
            PresedinteRomania()
        return PresedinteRomania.__instance

    def __init(self):
        if PresedinteRomania.__instance is not None:
            raise Exception("Exista deja functia de presedinte al Romaniei")
        else:
            PresedinteRomania.__instance = self


a = PresedinteRomania
print(a)
print(id(a))
b = PresedinteRomania
print(b)
print(id(b))
print(f"a = b? {a == b}")
"""


class PresedinteRomania:
    __instance = None

    def __new__(cls, *args, **kargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, nume):
        self.nume = nume

    def __str__(self):
        return f"Eu sunt {self.nume} presedintele Romaniei"

    # def say_hello(self):


a = PresedinteRomania("Magarel Ciucurete")
print(a)
b = PresedinteRomania("Gigel Frone")
print(b)
c = PresedinteRomania("Vanesa Contesa")
print(c)
print(f"a = b = c? {a == b == c}")
# c.nume("Marocanu XXl")
# print(c)
