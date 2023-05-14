"""
1.Funcție care să calculeze și să returneze suma a două numere
"""


def sum_of(number1, number2):
    return number1 + number2


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


def nr_of_chars1(full_name):
    nr_chars = 0
    full_name_splitted = full_name.split(" ")
    for name in full_name_splitted:
        for i in range(len(name)):
            nr_chars += 1
    return f"Your name: {full_name} has {nr_chars} characters in it"


def nr_of_chars2(full_name):
    nr_chars = 0
    for i in full_name:
        if i.isalpha():
            nr_chars += 1
    return f"Your name: {full_name} has {nr_chars} characters in it"


print(nr_of_chars1('Mihaila Octavian Dumitru'))
print(nr_of_chars1('Titi Aur'))
print(nr_of_chars2('Mihaila Octavian Dumitru'))
print(nr_of_chars2('Titi Aur'))
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


def get_area_of_circle(radius, color='gri'):
    pi = 3.14
    return f"Area of a circle with radius {radius} is {pi * radius**2} with {color}"


print(get_area_of_circle(10))
print(get_area_of_circle(3))
print()
print(get_area_of_circle(radius=2, color="mov"))
print(get_area_of_circle(4, "verde"))
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
        if i.isupper() and i.isalpha():
            x += 1
        elif i.islower() and i.isalpha():
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


month1 = "Mai"
month2 = "Decembrie"
month3 = "casd"

print(get_number_of_days(month1))
print(get_number_of_days(month2))
print(get_number_of_days(month3))
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
print('-' * 40)

"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""


def number_counter(*args):
    dict_counter = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in args:
        if i in dict_counter:
            dict_counter[i] += 1
    for i, j in dict_counter.items():
        print(f"{i}: {j}")
    return dict_counter


d = number_counter(1, 3, 1, 5, 9, 7, 7, 5, 5)
print(d)
print('-' * 40)

"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""


def get_max(*args):
    return max(args)


max1 = get_max(2, 3, 8)
print(max1)
print('-' * 40)

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""


def sum_of_number(x):
    total = 0
    for i in range(x+1):
        total += i

    return total


nr1 = sum_of_number(4)
nr2 = sum_of_number(6)
print(nr1)
print(nr2)
print('-' * 40)

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""


def common_numbers(first_list, second_list):
    common_set = set()
    for i in first_list:
        if i in second_list:
            common_set.add(i)
    return common_set


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
ex16_t1 = common_numbers(list1, list2)
print(ex16_t1)
print('-' * 40)

"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""


def get_discount(price, discount):
    if price != 0 and discount < 100:
        price = price * (1-discount/100)
        return f"Price after discount is {price}"
    else:
        return f"Invalid discount"


print(get_discount(100, 20))
print(get_discount(100, 100))
print(get_discount(0, 20))
print('-' * 40)

"""
 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)
"""

# import pytz
# from datetime import datetime
#
#
# def get_time_romania():
#     timezone_bucharest = pytz.timezone('Europe/Bucharest')    # cream un fus orar
#     datetime_bucharest = datetime.now(timezone_bucharest)     # folosim fusul creat pentru a ne da data si ora actuala
#     return f"Romania/Bucharest: {datetime_bucharest}"
#
#
# def get_time_china():
#     timezone_hong_kong = pytz.timezone('Asia/Hong_kong')
#     datetime_hong_kong = datetime.now(timezone_hong_kong)
#     return f"China/Hong_kong: {datetime_hong_kong}"
#
#
# print(get_time_romania())
# print(get_time_china())
# print("-" * 40)

"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici 
cand e ziua ta :)
"""

# import datetime
#
#
# def get_day_until_christmas():
#     current_date = datetime.date.today()
#     current_year = datetime.datetime.now().year
#     christmas_date = datetime.date(current_year, 12, 25)
#     if current_date > christmas_date:
#         christmas_date = datetime.date(current_year+1, 12, 25)
#         return f"Days remaining until Christmas {(christmas_date - current_date).days}"
#     else:
#         return f"Days remaining until Christmas {(christmas_date - current_date).days}"
#
#
# print(get_day_until_christmas())
