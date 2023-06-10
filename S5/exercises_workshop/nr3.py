"""
Implementați un generator pentru loteria 6/49 și noroc:
-	Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
-	Ultima apelare va da un singur număr de “noroc” format din 7 cifre

"""

# from random import randint
#
#
# def loterie(limit=7):
#     for i in range(limit):
#         if i < limit-1:
#             yield randint(1, 49)
#         else:
#             yield randint(1000000, 9999999)
#
#
# generator = loterie()
# nr_loterie = []
# for numar in generator:
#     nr_loterie.append(numar)
# print(nr_loterie)

import random


# def generator_loterie():
#     nr_generate = []
#     for i in range(6):
#         nr_random = random.randint(1, 49)
#         while nr_random in nr_generate:
#             nr_random = random.randint(1, 49)
#         nr_generate.append(nr_random)
#         yield nr_random
#
#
# g = generator_loterie()
#
# for nr in g:
#     print(nr)


def loto_gen():
    my_list = random.sample(range(1, 50), 6)
    for nr in my_list:
        yield nr
    yield random.randint(1_000_000, 9_999_999)


for nr in loto_gen():
    print(nr)
