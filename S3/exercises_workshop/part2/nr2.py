"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
●	descrie()
●	aria()
●	perimetrul()
●	schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și
    va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print()
        print(f"Dreptunghi de {self.lungime} X {self.latime}")
        print(f"Culoare: {self.culoare}")
        print(f"Aria de {self.aria():.2f}")
        print(f"Perimetru de {self.perimetrul():.2f}")
        print('-' * 40)

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return self.lungime * 2 + self.latime * 2

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare


d1 = Dreptunghi(10, 5, "Galben")
d1.descrie()
d1.schimba_culoare("Verde")
d1.descrie()
