"""
Functia print ne ajuta sa printam informatii in terminal
print(ceva, alteva, etc) <= putem afisa oricate chestii, cu virgula intre ele
"""
print("Adela", "Neacsu", "Hello", 1234, True)

nume = "Octavian"
print("Numele meu este " + nume)

# Functia print trece pe o linie noua la fiecare apelare
print("Numele meu este")
print(nume)

varsta = 24
# print("Varsta mea este: " + varsta) # va da eroare

#f-strings => un mod mai pythonic de a afisa variabile in mesajele noastre

print(f"Numele meu este {nume} si am varsta de {varsta}")

