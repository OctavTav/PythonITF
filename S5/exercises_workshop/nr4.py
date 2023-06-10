"""
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul,
folosind urmatoarele 2 metode:
-	try - finally
-	Fișierul se deschide înainte de try, folosind functia open
-	În interiorul try citim conținutul folosind functia read
-	În finally se închide fișierul
-	with (context manager)
-	Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul,
pentru ca context managerul face asta pentru noi.

"""

# try:
#     f = open('hello.txt', 'r')
#     lines = f.read()
#     print(lines)
# except:
#     print("error")
# finally:
#     f.close()

# with open('hello.txt') as my_file:
#     for line in my_file:
#         print(f'Line: {line}')

# try:
#     f = open('hello.txt')
# except IOError:
#     print("file not found")
# else:
#     for line in f:
#         print(f'Line: {line}')
# finally:
#     f.close()


# f = open('hello.txt')
# try:
#     for line in f:
#         print(f'Line: {line}')
# finally:
#     f.close()

f = open('hello.txt')
try:
    print(f.read())
finally:
    f.close()
