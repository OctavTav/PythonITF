"""
Slicing - operatie care ne permie sa accesam mai multe elemente dintr-o lista
sau dintr-un string (care este de fapt doar o lista de caractere

Sintaxa
lista[start:stop:pas] - pas este optional, valoarea lui default este 1
- start reprezinta indexul de la are incepem
- stop reprezinta indexul la cere ne oprim
- pas (step) reprezinta "viteza" cu care ne miscam de la start la stop
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = l[2:5]  #  obtinem elementele din lista originala de la index 2->5, 2 inclusiv, 5 exclusiv
print(l2)

l3 = l[5:2:-1]      # voi obtine [6, 5, 4]
print(l3)

l4 = l[0:len(l):2]  # voi obtine elementele de la indexi pari
print(l4)

"""
Daca start = inceput lista (sau finalul daca mergem cu pas negativ) putem sari peste
Daca stop = sfarsit lista (sau inceputul daca mergem cu pas negativ putem sari peste
"""
l5 = l[::2]     # echivalent cu 14
print(l5)

"""
O metoda foarte simpla de a inversa o lista este sa o parcurgem cu pas de -1
"""
lr = l[::-1]
print(lr)

"""
Deoarece stringurile sunt practic liste de caractere si ala ele se aplica aceleasi reguli de slicing!
"""
s = "Ana are mere"
print(s[3:10])
print(s[::2])

print(len(s))
print(s[10:100])    # nu va da eroare, dar vom primi doar caracterele existente pana la sfarsitul primului

# NU DENUMITI VARIABILELE LIST
# list = [100, 200]     #NO NO NO NO NO NO NO


