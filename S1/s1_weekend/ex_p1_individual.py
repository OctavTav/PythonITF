#   O variabila este ca o cutie ce poate stoca un anumit tip sau mai multe tipuri de date

# print("-"*100)

# var_string = "Octavian"
# var_int = 24
# var_float = 1.83
# var_bool = False
#
# print("-"*100)
#
# print(type(var_string))
# print(type(var_int))
# print(type(var_float))
# print(type(var_bool))
#
# print("-"*100)
#
# var_float = round(var_float)
# print(type(var_float))
#
# print("-"*100)
#
# print(f"Numele meu este {var_string}")
# print(f"Am varsta de {var_int} ani")
# print(f"Inaltimea mea rotunjita este de {var_float} metri")
# print(f"Statusul meu de casatorie este {var_bool}")
#
# print("-"*100)
#
# first_name = input("Prenumele meu este: ")
# last_name = input("Numele meu este: ")
#
# print(f"Numele complet are {len(first_name + last_name)} caractere")
#
# print("-"*100)
#
# width = float(input("Introdu o latime in metri: "))
# length = float(input("Introdu o lungime in metri: "))
# print(f"Aria dreptunghiului cu lungimea de {length} metri si latimea de {width} metri este de {length*width} metri patrati")
#
# print("-"*100)

# sentence = "Coral is either the stupidest animal or the smartest rock"
# word = " the "
# print(f"In expresia {sentence}, cuvantul ``{word}`` apare de  {sentence.count(word)} ori")
#
# assert sentence.isalpha(), "String-ul nu contine doar numere"
# return print("String-ul de mai sus")

# print("-"*100)

# while True:
#     string_11 = input("Indrodu un string cu o dimensiune impara:\n")
#     if len(string_11) % 2 != 0 and len(string_11) >= 3:
#         mid_letter_pos = int(len(string_11) / 2)
#         print(f"Caracterul din mijlocul string-ului este: {string_11[mid_letter_pos]}")
#         break
#     else:
#         print(f"Introdu string cu dimeniunea impara si mai mare de 3!")

# print("-"*100)

# string_12 = input("Introduceti un string gen `alabala portocala`:\n")
# string_separat = string_12.split()
# print(string_separat)
# for i in string_separat:
#     print(i)

# print("-"*100)

# string_13 = input("Introduceti un string gen `alabala portocala`:\n")
# first_letter = string_13[0]
# string_modified = ""
# counter = 0
# for i in string_13:
#     if counter != 0 and string_13[counter] == first_letter and counter != len(string_13)-1:
#         string_modified += i.upper()
#     else:
#         string_modified += i
#     counter += 1
#
# print(f"String-ul modificat este:\n{string_modified}")

# print("-"*100)

user_id = input("Introduceti numele user-ului:\n")
pwd_id = input("Introduceti parola user-ului:\n")

# pwd_length = len(pwd_id)
#
# print(f"Parola pentru user-ul: {user_id} este {'*' * pwd_length} si are {pwd_length} caractere")
print(f"Parola pentru user-ul: {user_id} este {'*' * len(pwd_id)} si are {len(pwd_id)} caractere")