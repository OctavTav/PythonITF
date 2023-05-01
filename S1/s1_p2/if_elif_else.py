"""
If ne permita sa decidam  daca o anumita bucata de cod se executa sau nu

Sintaxa

if conditie_1:
    cod_1
elif conditie_2
    cod_2
else
    cod_3
"""

age = 19
print("Inainte de if")

if age > 18:
    print("Esti major")
    print("Felicitari!")

print("Dupa if")

print("_" * 80)

# nota_trecere = 5
# nota_primita = int(input("Introdu nota primita:\n"))
# if nota_primita >= nota_trecere:
#     print("Felicitari, ai trecut!")
# else:
#     print("Ghinion, ai picat!")
#
# print("_" * 80)

"""
Putem avea oricate nivele de imbricare pentru if-uri, DAR prea multe nu sunt in ok
Rule of thumb: 3 nivele de identare sunt suficiente, daca sunt necesare mai multe nivele ar trebui sa gasim
alta solutie

"""

if age >= 18:
    print("Esti major")
    if age >= 65:
        print("Esti pensionar")
        if age > 100:
            print("Esti centagenar")
    else:   # daca varsta este mai mica de 65
        print("Esti adult, nu pensionar")


"""
elif - else + if

if conditie_1:
    cod_1
elif conditie_2:
    cod_2
...
else
    cod_x - executat in cazul in care nici o conditie nu este intalnita
"""

years_of_experience = int(input("Introdu anii de experienta:\n"))

if years_of_experience == 0:
    print("Esti intern, poti merge la un internship")
elif years_of_experience < 2:
    print("Esti junior, salariul tau este 4000")
elif years_of_experience < 5:
    print("Esti mid, salariul tau este 8000")
elif years_of_experience < 10:
    print("Esti senior, salariul tau este 12000")
else:
    print("Felicitari, esti pensionar!")

