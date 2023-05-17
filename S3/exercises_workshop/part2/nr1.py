"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
●	descrie_cerc() - va PRINTA culoarea și raza
●	aria() - va RETURNA aria
●	diametru()
●	circumferinta()
"""


class Cerc:
    pi = 3.14

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f"Culoarea cercului: {self.culoare}")
        print(f"Raza cercului: {self.raza}")

    def aria(self):
        return self.pi * (self.raza ** 2)

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return 2 * self.raza * self.raza


c1 = Cerc(5, "Rosu")
c1.descriere_cerc()
print(f"Aria: {c1.aria()}")
print(f"Circumferinta: {c1.circumferinta()}")
