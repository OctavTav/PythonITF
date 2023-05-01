

grade = float(input("Introdu nota:\n"))
american_grade = ""


"""
In general, input checks sunt PRIMELE chestii pe cale fe facem:
fail-test, daca utilizatorul ea introdus date gresite, vrem sa "scapam"
de acest use-case cat mai repede:
"""

# if grade > 10 or grade <= 0:
#     print("Ai introdus o valoare gresita!")
# else:
#     if grade  <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade < 8:
#         american_grade = "C"
#     elif grade < 9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#
#     print(f"Felicitari ai luat nota {american_grade}")

x = int(input("Introdu x:\n"))
y = int(input("Introdu y:\n"))
z = int(input("Introdu z:\n"))

max_number = x     # presupunem ca valoarea maxima este x

if max_number < y:
    max_number = y
if max_number < z:
    max_number = z

print(f"Numarul maxim este {max_number}")
print(f"Verificare  {max(x, y, z)}")

"""
Solutia 2: fara folosirea unei variabile auxiliare:
"""
if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)

"""
Solutia 3: cu if-uri imbricate si fara variabile aux
"""

if x >= y:
    if x >= z:
        print(x)
    else:
        print(z)
else:
    if y >= z:
        print(y)
    else:
        print(z)
