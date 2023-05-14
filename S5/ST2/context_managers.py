"""
Context manager = o implemantare care ne permite sa gestionam resurse contextual
Exemple de resurse: fisiere, conexiuni la db (data base), conexiuni la sv(server)

In general, aceste tipuri de resurse trebuie sa fie deschisse si mai apoi inchise


Cel mai utilizat  context manager este with.

with deschide(ceva) as handler:
    fa ceva cu handler...
# aici, dupa ce s-a terminat cu blocul with, NU vom mai avea acces la handler

ECHIVALENT CU

handler = deschide(ceva) => conexiune la db, fisier, etc
fa ceva cu handler
inchide(ceva)

"""

f = open('myfile.txt')    # deschidem un fisier pentru citire
lines = f.readlines()       # citim toate liniile din fisier
print(lines)                # le afisam
f.close()                   # IMPORTANT : inchidem fisierul

with open('myfile.txt') as my_file:
    for line in my_file:
        print(f'Line: {line}')


# Aici va da eraore, deoarece context managerul with a inchis deja fisierul
print(my_file.readlines()) # va da ValueErrorL I/O operation on closed file
