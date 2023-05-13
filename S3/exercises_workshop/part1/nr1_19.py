"""
1.Funcție care să calculeze și să returneze suma a două numere
"""


def sum_of(nr1, nr2):
    return nr1 + nr2


print(sum_of(5, 3))
print(sum_of(-1, 3))
print("-" * 40)

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
"""


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(f"3 este par?: {is_even(3)}")
print(f"4 este par?: {is_even(4)}")
print("-" * 40)

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu) 
"""


def nr_of_chars(full_name):
    nr_chars = 0
    full_name_splitted = full_name.split(" ")
    for name in full_name_splitted:
        for i in range(len(name)):
            nr_chars += 1
    return f"Your name: {full_name} has {nr_chars} characters in it"


print(nr_of_chars('Mihaila Octavian Dumitru'))
print(nr_of_chars('Titi Aur'))
print("-" * 40)

"""
4. Funcție care returnează aria dreptunghiului
"""


def get_area_of_rectangle(length, width):
    return f"The area of a rectangle {length} by {width} is: {length * width}"


print(get_area_of_rectangle(3, 6))
print(get_area_of_rectangle(10, 6))
print("-" * 40)

"""
5. Funcție care returnează aria cercului
"""


def get_area_of_circle(radius):
    PI = 3.14
    return f"Area of a circle with radius {radius} is {PI * radius**2}"


print(get_area_of_circle(10))
print(get_area_of_circle(3))
print("-" * 40)

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""


def search_char(char_searched, string_of_char):
    print(f"Is char {char_searched} in {string_of_char}?")
    if char_searched in string_of_char:
        return True
    else:
        return False


print(search_char('a', 'Ciricirel Combustie'))
print(search_char('a', 'Ana are mere'))
print("-" * 40)

"""
7. Funcție fără return, primește un string și printează pe ecran:
●	Numărul de caractere lower case este x
●	Numărul de caractere upper case exte y 
"""


def nr_lowers_uppers(string_given):
    x = 0
    y = 0
    for i in string_given:
        if i == i.upper() and i.isalpha():
            x += 1
        elif i == i.lower() and i.isalpha():
            y += 1
    print(f"In {string_given} we have:")
    print(f"{x} characters that are lower case")
    print(f"{y} characters that are upper case")


nr_lowers_uppers("Gigel")
nr_lowers_uppers("asfA SFkpiA SFi")
print('-' * 40)

"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""


def get_positives_only(list_given):
    positive_numbers = []
    for i in list_given:
        if i >= 0:
            positive_numbers.append(i)
    return positive_numbers


list1 = [2, 1, 123, 1, -2, 2, 12, 0, -4, -6, -7]
list2 = [2, 7, 29, -12, 0, 2, -5, -7]
print(get_positives_only(list1))
print(get_positives_only(list2))
print('-' * 40)

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
●	Primul număr x este mai mare decat al doilea număr y
●	Al doilea număr y este mai mare decat primul număr x
●	Numerele sunt egale. 
"""


def compare(x, y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
    elif x < y:
        print(f"Al doilea numar {y} este mai mare decat primul {x}")
    else:
        print("Numerele sunt egale")


compare(4, 5)
compare(-1, -2)
print('-' * 40)

"""
10. Funcție care primește un număr și un set de numere.
●	Printează ‘am adaugat numărul nou în set’ + returnează True
●	Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""


def add_number(number, numbers_set):
    if number not in numbers_set:
        numbers_set.add(number)
        print("Am adaugat numarul nou in set")
        return True
    else:
        print("Nu am adaugat numarul in set. Acesta exista deja")
        return False


set_numbers = {1, 2, 3, 4, 5, 6, 7}
print(f"Adaugam 7 in set? {add_number(7, set_numbers)}")
print()
print(f"Adaugam 8 in set? {add_number(8, set_numbers)}")
print('-' * 40)

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună
"""


def get_number_of_days(luna):
    an = {
        'Ianuarie': 31,
        'Februarie': 28,
        'Martie': 31,
        'Aprilie': 30,
        'Mai': 31,
        'Iunie': 30,
        'Iulie': 31,
        'August': 31,
        'Septembrie': 30,
        'Octombrie': 31,
        'Noiembrie': 30,
        'Decembrie': 31
    }
    if luna in an:
        return f"Luna {luna} are {an[luna]} zile"
    else:
        return f"Luna {luna} nu exista"


luna1 = "Mai"
luna2 = "Decembrie"
luna3 = "casd"

print(get_number_of_days(luna1))
print(get_number_of_days(luna2))
print(get_number_of_days(luna3))
print('-' * 40)

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
●	print("Suma: ", a)
●	print("Diferenta: ", b)
●	print("Inmultirea: ", c)
●	print("Impartirea: ", d)
"""


def calculator(x, y):
    suma = x + y
    diferenta = x - y
    inmultire = x * y
    impartire = x / y

    return suma, diferenta, inmultire, impartire


a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
