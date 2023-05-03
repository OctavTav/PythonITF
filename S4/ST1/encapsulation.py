"""
Encapsualtion = notiunea de a tine toate atributele si metodele  relevante pt un obirct in clasa acestuia
si de a le afisa/ascunde in functie de nevoi

Avem 3 tipuri de modificatori care ne dau vizibilitatea atributelor si metodelor:
    - privat : atribute si metode care NU sunt deloc vizibile in afara clasei in care sunt definite
    - protected : atribute si metode care sunt vizibile doar in clasa curenta si in clasele care o
                mostenesc pe cea curenta; acestea incep cu un singur underscore => acesta este doar un standard
    - public : atribute si metode vizibile de oriunde
"""

class Person:

    def __init__(self, cnp, name, age, height, ):
        self.__cnp = cnp    # atributul __cnp este privat, nu putem citi nici scrie din afara clasei
        self._name = name   # atributul _name este "protected", adica nu ar trebui sa il accesam decat din clasele copil
        self.age = age
        self.height = height

    def describe(self):
        print(f"{self.__cnp} : {self._name}, {self.age} ani, {self.height}m")

    # acesta se numeste getter deoarece expune valoarea in afara clasei
    @property       # decorator special ca sa nu mai punem () cand folosim functia (ion.cnp)
                    # transforma o metoda intr-un atribut
    def cnp(self):
        print("This is a getter")
        return self.__cnp

    # setter = metoda care ne permite sa scriem o valoare intr-un atribut privat
    @cnp.setter         # @nume_atribut.setter va face ca aceasta metoda sa actioneze ca un setter
    def cnp(self, new_cnp):
        print("This is a setter")
        if len(new_cnp) == 13:
            self.__cnp = new_cnp
        else:
            print("Invalid CNP value, should be 13 chars long.")

    def __private_method(self):
        pass

    #doar pentru atributele definite cu @property putem avea setter si deleter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    # Va fi apelat atunci cand incercam sa stergem proprietatea folosind functia del
    @name.deleter
    def name(self):
        print("Trying to delete not possible")



ion = Person('1234567890123', 'Ion Popescu', 25, 1.80)
ion.describe()
#   print(ion.__cnp)   # va da atribute error 'Person' object has no attribute '__cnp'
ion.__cnp = 'cnp nou'   # nu va modifica __cnp, deoarece nu il poate "vedea"
ion.describe()

print(ion.cnp)
ion.cnp = 'altceva nou'     # va da eroare daca nu avem setter AttributeError: can't set

ion.describe()
# ion.__private_method()      # nu vede metoda AttributeError: 'Person' object has no attribute '__private_method'

print('-' * 40)
print(ion.name, ion._name)       # va afisa numele, dar nu ar trebui sa accesam in felul acesta
ion._name = 'Gheorghe Popescu'      # va merge dar nu ar trebui sa facem asa
ion.describe()

print('*' * 40)
# In mod normal, putem sterge un atribut de pe un obiect folosint del

del ion.name
ion.describe()