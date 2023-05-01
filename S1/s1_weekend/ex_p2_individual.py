import random

# 1-------------------------------------------------------------
"""
Functia if else poate fi comparata cu bifurcatie de drumuri, daca se indeplineste conditia atunci
continuam pe un drum, daca nu vom continua pe celalalt
Daca nu e laie, e balaie
"""
print("-"*70)

# 2-------------------------------------------------------------
# while True:     # oblig user-ul sa introduca valori numerice
#     x = input("Introdu valoarea lui x: ")
#     if not x.isalpha():     # am incercat cu is.digit() si is.decimal, dar cand scrii nr cu zecimala o ia pe ulei
#         x = float(x)
#         if x == round(x) and x >= 0:
#             x = round(x)
#             print(f"Numarul {x} este natural")
#             break
#         else:
#             print(f"Numarul {x} nu este natural")
#             break
#     else:
#         print("Introdu valori numerice!")

print("-"*70)

# 3-------------------------------------------------------------
# while True:
#     x = input("Introdu valoarea lui x: ")
#     if not x.isalpha():
#         x = float(x)
#         if x > 0:
#             print(f"{x} este pozitiv")
#             break
#         elif x == 0:
#             print(f"{x} este neutru")
#             break
#         else:
#             print(f"{x} este negativ")
#             break
#     else:
#         print("Introdu valori numerice!")

print("-"*70)

# 4-------------------------------------------------------------
# while True:
#     x = input("Introdu valoarea lui x: ")
#     if not x.isalpha():
#         x = float(x)
#         if x > -2 and x < 13:
#             print(f"{x} este intre -2 si -13")
#             break
#         else:
#             print(f"{x} nu este intre -2 si -13")
#             break
#     else:
#         print("Introdu valori numerice")

print("-"*70)

# 5 - tema de casa-------------------------------------------------------------
# while True:
#     x = input("Introdu valoarea lui x: ")
#     y = input("Introdu valoarea lui y: ")
#     try:
#         x = float(x)
#         y = float(y)
#     except:
#         print("Mai incearca!")
#         continue
#     if x - y < 5:
#         print(f"Diferenta dintre {x} si {y} este mai mica 5, mai exact {x-y}")
#         break
#     else:
#         print(f"Diferenta dintre {x} si {y} nu este mai mica de 5, este {x-y}")
#         break


print("-"*70)

# 6 - tena de casa-------------------------------------------------------------
# while True:
#     x = input("Introdu valoarea lui x: ")
#     try:
#         x = float(x)
#     except:
#         print("Mai incearca")
#         continue
#     if not (5.0 < x < 27.0):
#     # if not (5 < x 27):        # scriem asa daca vrem ca intervalul sa fie doar cu numere intregi
#                                      # sau if x not in range(5 < x < 27)
#         print(f"{x} nu se afla in intervalul (5,27)")
#         break
#     else:
#         print(f"{x} se afla in intervalul (5,27)")
#         break

#
print("-"*70)
# 7-------------------------------------------------------------
# while True:
#     x = input("Introdu o valoare intreaga pozitiva pentru x: ")
#     y = input("Introdu o valoare intreaga pozitiva pentru y: ")
#     try:
#         x = int(x)
#         y = int(y)
#     except:
#         print("Mai incearca")
#         continue
#     if x != y:
#         print(f"Numarul mai mare este {max(x,y)}")
#         break
#     else:
#         print(f"Numerele sunt egale!")
#         break


print("-"*70)
# 8-------------------------------------------------------------
print("Introdu lungimile laturilor unui triunghi:")
# while True:
#     a = input("a = ")
#     b= input("b = ")
#     c = input("c = ")
#     try:
#         a = float(a)
#         b = float(b)
#         c = float(c)
#     except:
#         print("Mai incearca")
#         continue
#     if a > 0 and b > 0 and c > 0:
#         if a == b == c:
#             print("Triunghiul este echilateral")
#             break
#         elif a == b or a == c or b == c:
#             print("Triunghiul este isoscel")
#             break
#         else:
#             print("Triunghiul este oarecare")
#             break
#     else:
#         print("Nu exista triunghi cu lungimi ale laturilor negative sau egale cu 0")



print("-"*70)
# 9-------------------------------------------------------------

print("-"*70)
# 10-------------------------------------------------------------

print("-"*70)
# 11-------------------------------------------------------------

print("-"*70)
# 12-------------------------------------------------------------

print("-"*70)
# 13-------------------------------------------------------------

print("-"*70)
# 14-------------------------------------------------------------

print("-"*70)
# 15-------------------------------------------------------------

print("-"*70)
# 16-------------------------------------------------------------

print("-"*70)
# 17-------------------------------------------------------------

print("-"*70)
# 18-------------------------------------------------------------

print("-"*70)
# 19-------------------------------------------------------------

# print("Ready for a round of Dice? Yes/No ")
# while True:
#     choice_check = input("")
#     if choice_check.lower() != "no":
#         print(choice_check)
#         roll_dice = random.randint(1, 6)
#         # print(roll_dice)
#         user_guess = int(input("Guess the computer's roll: "))
#         if user_guess == roll_dice:
#             print("Congrats! You guessed it!")
#         else:
#             print(f"Such shame! Much sad! The roll was {roll_dice}")
#     else:
#         print("Byeeee!")
#         break
#     print("Wanna play again? Yes/No")

print("-"*70)
# 20-------------------------------------------------------------

print("-"*70)
# 21-------------------------------------------------------------



