from abc import ABC, abstractmethod
"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

"""

"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
"""

"""
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte 
(opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""

"""
POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

3. Actualizează proiectul pe github facand un push la noul cod
În Folderul de teme ajunge să pui doar linkul cu proiectul tău public
"""


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probail am colturi")


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    # aici cream getter, ca sa putem folosi variabila ~__latura~ care este privata
    @property
    def latura(self):
        return self.__latura

    # aici cream setter, ca sa putem modifica variabila ~__latura~ care este privata
    @latura.setter
    def latura(self, latura_noua):
        self.latura = latura_noua

    # aici cream deleter DAR doar incercam sa stergem, alfel vor aparea erori
    @latura.deleter
    def latura(self):
        print("Trying to delete 'latura'")
        # self.latura = 0
        # self.latura = None

    def aria(self):
        return self.latura ** 2


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        self.raza = raza_noua

    @raza.deleter
    def raza(self):
        print("Trying to delete 'raza'")
        # self.raza = 0
        # self.raza = None

    def aria(self):
        return self.pi * (self.raza ** 2)

    def descrie(self):
        print("Eu nu am colturi")


p1 = Patrat(5)
p1.descrie()
del p1.latura
c1 = Cerc(10)
c1.descrie()
del c1.raza
