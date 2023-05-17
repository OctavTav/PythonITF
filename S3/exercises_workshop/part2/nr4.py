"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
●	afisare_sold() - Titularul x are în contul y suma de n lei
●	debitare_cont(suma)
●	creditare_cont(suma)
"""


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = str(iban)
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titular cont: {self.titular_cont}")
        print(f"Sold curent: {self.sold}")
        print('-' * 40)

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f"Suma debitata {suma}")
        print('-' * 40)

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"Suma creditata {suma}")
        print('-' * 40)


c1 = Cont(123, 'Georgica Buturuga', 10000)
c1.afisare_sold()
c1.debitare_cont(1200)
c1.creditare_cont(3000)
c1.afisare_sold()
