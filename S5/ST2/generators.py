"""
Genratori = o madalitate simpla de a genera valori care pot fi parcurse secvential
Dpdv al sintaxeo, generatorii sunt functii care folosesc cuvantul cheie yield pentru a da inapoi o valoare
codlui care i-a apelat

Spere deosebire de o  functie normala, care ori de cate ori este apelata, ea va fi executata de la inceput,
generatorii vor continua dupa yield

Yield = a ceda prioritate
"""


def funct_gen():
    print("Am intrat in functia generator")
    yield 10        # aici functia noastra generator va returna o valoare (10)

    print("Am intrat din nou in functia generator")
    yield 100       # aici a doua valoare returnata

    print("Am intrat din nou in functia generator")


gen = funct_gen()

print(next(gen))
print(next(gen))
# print(next(gen))        # va da eroare StopIteration, deoarece nu ajunge la nici o instructiune yield

"""
Generatorii sunt foarte utili, deoarece ei pot "crea" valori noi la fiecare apelare
si consuma putina memorie.
Spre deosebire de iteratori, generatorii pot rula la infinit (desi nu e indicat).
De asemenea, sunt mult mai usor de implementat decat iteratorii
"""

# facem un generator ce ne face patrate perfecte
def pp(limit = 20):
    p = 0
    while p <= limit:
        yield p ** 2
        p += 1


gen_pp = pp()
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))
print(next(gen_pp))

print("-" * 40)

for val in gen_pp:
    print(val)
