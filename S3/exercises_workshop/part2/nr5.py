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

    def __init__(self, numar):
        self.numar = numar
        self.date = None
        self.total_produs = None
        self.pret_buc = None
        self.cantitate = None
        self.lista_produse = {}
        self.nume_produs = None
        self.total_plata = None

    def adauga_produs(self, nume_produs, cantitate, pret_buc):
        self.lista_produse[nume_produs] = list()
        self.lista_produse[nume_produs].append(cantitate)
        self.lista_produse[nume_produs].append(pret_buc)
        self.lista_produse[nume_produs].append(self.get_total_produs(nume_produs))

    def get_total_produs(self, nume_produs):
        return self.lista_produse[nume_produs][0] * self.lista_produse[nume_produs][1]

    def schimba_cantitatea(self, nume_produs, cantitate):
        self.lista_produse[nume_produs][0] = cantitate
        self.lista_produse[nume_produs][2] = self.get_total_produs(nume_produs)

    def schimba_pretul(self, nume_produs, pret):
        self.pret_buc = pret
        self.lista_produse[nume_produs][2] = self.get_total_produs(nume_produs)

    def sterge_produsul(self, nume_produs):
        del self.lista_produse[nume_produs]

    def schimba_numele_produsului(self, nume_produs, nume_nou):
        self.lista_produse[nume_nou] = self.lista_produse[nume_produs]
        self.sterge_produsul(nume_produs)

    def get_date(self):
        self.date = datetime.today()
        return self.date

    def genereaza_factura(self):
        self.total_plata = 0
        print(f"Factura seria {self.serie} numar {self.numar}")
        print(f"Data: {self.get_date()}")
        col1, col2, col3, col4 = "Produs", 'Cantitate', 'Pret bucata', 'Total produs'
        col_size = 20

        print(f"{col1:^{col_size}}|{col2:^{col_size}}|{col3:^{col_size}}|{col4:^{col_size}}|")
        for produs in self.lista_produse.keys():
            print(f"{str(produs):^{col_size}}", end="|")
            for coloana in self.lista_produse[produs]:
                print(f"{str(coloana):^{col_size}}", end="|")
            print()
        for produs in self.lista_produse.keys():
            self.total_plata += self.lista_produse[produs][2]
        print('-' * 4 * col_size)
        print(f"Total de plata: {self.total_plata}")
        print('-' * 4 * col_size)


f1 = Factura(1)
f1.adauga_produs('Telefon', 7, 700)
f1.adauga_produs('TV', 1, 2000)
f1.adauga_produs('Frigider', 2, 1500)
f1.genereaza_factura()
f1.schimba_cantitatea('TV', 5)
f1.genereaza_factura()
f1.schimba_pretul('Telefon', 1000)
f1.genereaza_factura()
f1.schimba_numele_produsului('Frigider', 'Congelator')
f1.genereaza_factura()
f1.sterge_produsul('TV')
f1.genereaza_factura()
