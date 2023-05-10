"""
Structural Design Patterns

Adapter
Bridge
Composite = folosit pentru a crea o ierarhie de obiecte, in care obiectele au  atribute si functionalitati comune
    dar, au si o relatie de genul copil-parinte intre ele. Cele mai de la baza obiecte se numesc "Leaf"
    deoarece atunci cand folosim design pattern Composite, strucura acestor componente va arata ca un arbore
    Ex1: locatii(avem tara, judet, municipiu, oras, comuna, sat etc) - > fiecare dintre aceste locatii
        are un nume, coordonate GPS, populati, etc, DAR in acelasi timp au si o relatie intre acestea,
        deoarece tara are mai multe judetem fiecare judet are orase si comune, samd
    Ex2: categorii intr-un magazin virtual:
        Electrocasnice
            Mari
                Frigidere
                Masini de spalat
            Mici
                Toaster
                Cuptoare microunde
                    Incorporabile -> Leaf, nu mai exista alte subcategorii
                    Normale
            Personale
        Alimente
            Fructe Legume
            Conserve

Decorator = folosit pentru a augmenta functionaliatea unei metode/functii, in Python avem decoratorii
    cu sintaxa @something pe linia de dinaintea functiei pe care vrem sa o "decoram"
    Acesti decoratori sunt apelati inainte de functia propriu-zisa, si ne pot oferi informatii extra de pe aceasta

Facade
Flyweight
Private Class

Proxy = folosit atunci  cand vrem sa avem un wrapper pentru un anumit serviciu, care sa faca anumite
    pre-procesari necesare pentru utilizarea serviciului repectiv
    In general se foloseste cand vorbim despre web si cand avem conexiuni in retea

"""

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = [] # object pot fi alte foldere sau fisiere

    @property
    def size(self):
        total_size = 0
        for obj in self.children:
            total_size += obj.size
        return total_size

    def add_child(self,child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def print_structure(self, level = 0):
        print(f"Folder {self.name}{self.size} KB")




class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

root = Folder('root')
a = Folder('a')
b = Folder('b')
root.add_child(a)
root.add_child(b)

f1 = File('ceva text', 100)
f2 = File('altceva', 50)
a.add_child(f1)
b.add_child(f2)

f3 = File('asfasf', 220)
f4 = File('asas', 80)
c = Folder('c')
b.add_child(f3)
b.add_child(f4)
b.add_child(c)

f5 = File('asd', 50)
c.add_child(f5)

