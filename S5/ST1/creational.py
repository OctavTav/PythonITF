"""
Factory => folosit atunci cand avem mai multe clase cu o implementare comuna, care pot fi folosite
            interschimbabil in cod (ex UserFactory => User de tip admin sau un user regular, in functie de cine face
            login intr-un sistem. In general, Factory se foloseste impreuna cu Inheritance sau  Abstraction
Abstract Method
Builder
Singleton
Object Pool => folosit in situatii in care avem o clasa la care crearae (instantierea) de obiecte este foarte
                heavy dpdv computational.
Prototype => folosit cand avem mai multe obiecte similare

1. Singleton = desgn care ne permite sa avem o clasa care mereu returneaza aceeasi instanta unica
De obicei il folosim in situatii in care nu ne intereseaza obiectul in sine, ci doar anumite functionalitati
(metode) ale  acestuia.

Exemplu: cand avem un logger pentru un proiect (adica o clasa care logheaza
"""


class Car:
    def __init__(self):
        pass


c1 = Car()
c2 = Car()
"""
c1 si c2 sunt obiecte DIFERITE, adica au ID-uri diferite, si se afla in locatii de memorie diferite
"""
print(id(c1))
print(id(c2))
print(c1 == c2)


class SingletonLogger:
    __instance = None   # atributul de clasa __instance va actiona ca un "obiect" fals
                        # pe care noi il vom returna de fiecare data cand se incearca crearea unui nou
                        # obiect din aceasta clasa
    """
    Functia init in Python nu este chiar construcoturl de-facto, ci este un initializator.
    Inainte de  aceasta functie, este de fapt apelata functia __new__, unde se creaza un obiect in realitate
    """
    def __new__(cls, *args, **kwargs):
        # Functia new nu are self ca si prim paramentru, pentru ca self inca nu exista la moment de runtime
        # In schimb, avem cls ca prim argument, care este de falt clasa curenta
        if cls.__instance is None:
            # prima data cand este cerut un nou obiect,trebuie sa il cream
            cls.__instance = object.__new__(cls)
        # apoi il returnam, acelasi obiect de fiecare data
        return cls.__instance


print('-' * 40)
s1 = SingletonLogger()
s2 = SingletonLogger()
s3 = SingletonLogger()

print(id(s1))
print(id(s2))
print(id(s3))

# s1, s2 si s3 sunt de fapt acelasi obiect, ADICA referinte catre acelasi loc in memorie
print(s1 == s2)
s1.logger_level = 'DEBUG'
print(s2.logger_level)