"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
●	descrie()
●	nume_complet()
●	salariu_lunar()
●	salariu_anual()
●	marire_salariu(procent)
"""


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print()
        print(f"Angajat: {self.nume_complet()}")
        print(f"Salariu_lunar: {self.salariu_lunar()} Lei")
        print(f"Salariu_anual: {self.salariu_anual()} Lei")
        print('-' * 40)

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu *= (1 + procent/100)
        return self.salariu


a1 = Angajat('Gogu', 'Ionel', 2300)
a2 = Angajat('Gigel', 'Frone', 2300)
a1.descrie()
a2.descrie()
a1.marire_salariu(20)
a1.descrie()
