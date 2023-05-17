"""
5. Clasa Factură
     Atribute:  seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie),
                număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
●	schimbă_cantitatea(cantitate)
●	schimbă_prețul(pret)
●	schimbă_nume_produs(nume)
●	generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000
"""
from datetime import datetime

# print(datetime.today())


class Factura:
    serie = 'A0001'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
        self.date = None
        self.total_produs = None
        self.produse = {
            self.nume_produs: None,
            self.cantitate: None,
            self.pret_buc: None,
            self.total_produs: None
        }

    def schimba_cantitatea(self, cantitatea):
        self.cantitate = cantitatea

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_numele_produsului(self, nume_nou):
        self.nume_produs = nume_nou

    def get_date(self):
        self.date = datetime.today()
        return self.date

    def genereaza_factura(self):
        print(f"Factura seria {self.serie} numar {self.numar}")
        print(f"Data: {self.get_date()}")
        print(f"Produs {' ' * (len(self.nume_produs) - 6)} | Cantitate | Pret bucata | Total")
        print(self.produse)


f1 = Factura(1, 'Telefon', 7, 700)
f1.genereaza_factura()
