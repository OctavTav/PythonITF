"""
Mostenire = avem o clasa parinte, si clase copil, iar clasele copil mostenesc atributele
            si metodele de la parinte

Mostenire se foloseste de obicei cand avem mai multe clase care au elemente comune(atribute, metode),
si nu vrem sa repetam codul comun aiurea

clasa Parent:
    ....

clasa Child(Parent)
    ....

In general, ne referim la clasa parinte ca si superclass, iar clasele copil sunt subclasses
De aceea, cand avem nevoie de o metoda din parinte, vom folosi sintaxa cu super()

Pentru a cauta o metoda sau un atribut, Pytpon se uita intai in clasa curenta, apoi in parinte,
bunic, strabunic, etc. Nu exista limitare la numarul de nivele la care se poate face mostenire
"""


class Vehicle:

    def __init__ (self, nr_wheels, color, doors_cnt):
        self.nr_wheels = nr_wheels
        self.color = color
        self.doors_cnt = doors_cnt

    def drive(self):
        print("I'm driving and I'm a vehicle")

    def describe(self):
        print(f"I'm a {self.color} vehicle, I have {self.nr_wheels} wheels and i have {self.doors_cnt} doors")


class Car(Vehicle):
    def __init__(self, color, doors_cnt):
        super(Car, self).__init__(4, color, doors_cnt)


class RedCar(Car):
    def __init__(self, doors_cnt):
        super().__init__('red', doors_cnt)


class BlueCar(Car):
    def __init__(self, doors_cnt):
        super().__init__('red', doors_cnt)


class Motorcycle(Vehicle):
    def __init__(self, color, needs_license=True):
        super(Motorcycle, self).__init__(2, color, 0)
        self.needs_license = needs_license

    def describe(self):
        # cand facem o metoda in interiorul clase copil identica cu cea din clasa parinte,
        # zicem ca SUPRASCRIEM meota (override)
        super(Motorcycle, self).describe()      # cu super() apelam practic metoda de la parinte
        print(f"Do you need a license to drive me? {self.needs_license}")


class Truck(Vehicle):
    def __init__(self, color):
        super(Truck, self).__init__(16, color, 2)


c = Car('blue', 4)
m = Motorcycle('red')
t = Truck('black')

c.describe()
m.describe()
t.describe()

red_car = RedCar(2)
red_car.describe()

blue_car = BlueCar(2)
blue_car.describe()