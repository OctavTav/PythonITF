"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
●	descrie()
●	aria()
●	perimetrul()
●	schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""


class Dreptunghi:                                   # cream clasa
    def __init__(self, lungime, latime, culoare):   # definim atributele in constructor
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def aria(self):                                 # calculam aria si o returnam
        return self.latime * self.lungime

    def perimetru(self):
        return (self.latime + self.lungime) * 2     # calculam perimetrul si il returnam

    def descrie(self):
        print()
        print(f"Dreptunghi cu lungimea {self.lungime} si latimea {self.latime}")
        print(f"Aria dreptunghiului este: {self.aria()}")
        print(f"Perimetrul dreptunghiului este: {self.perimetru()}")
        print(f"Culoarea dreptunghiului este: {self.culoare}")
        print()

    def schimba_culoarea_input(self):       # suprascriem culoarea obiectului curent
        self.culoare = input("Noua culoare va fi: ")

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


d1 = Dreptunghi(2, 10, "ROSU")
d2 = Dreptunghi(7, 10, "VERDE")
d1.descrie()
d2.descrie()
d1.schimba_culoarea("ROZ BONBON")
d1.descrie()

d1.schimba_culoarea_input()
d1.descrie()
