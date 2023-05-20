from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        if not isinstance(self, Cerc):
            print("Cel mai probabil am colturi")
        else:
            print("Eu nu am colturi")


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        # print("Patrat latura getter")
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        self.latura = latura_noua

    @latura.deleter
    def latura(self):
        print("Trying to delete `latura`")

    def aria(self):
        return self.latura ** 2

    def descrie(self):
        super().descrie()
        print(f"Am latura egala cu: {self.latura}")
        print(f"Am aria egala cu: {self.aria()}")


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
        print("Tryng to delete `raza`")

    def aria(self):
        return self.pi * (self.raza ** 2)

    def descrie(self):
        super().descrie()
        print(f"Cerc de raza {self.raza}")
        print(f"Aria egala cu: {self.aria()}")


p1 = Patrat(5)
p1.descrie()
c1 = Cerc(10)
c1.descrie()
