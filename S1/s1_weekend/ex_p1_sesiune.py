# 1 ------------------------------

print("-"*70)

# 2 ------------------------------
mountain = "Everest"
elevation = 8848
steps = 16.900
highest_mountain = True
print(f"Here are some information about Everest: {mountain} {elevation} {steps} {highest_mountain}")

print("-"*70)

# 3 ------------------------------
exercitiu = 3
timp = 10.5
corect = True
despre = "functia type"
print(type(exercitiu))
print(type(timp))
print(type(corect))
print(type(despre))

print("-"*70)

# 4 Exercitiu individual
var_4 = float(input("Introdu o valoarea cu zecimale:\n"))
valoare = var_4
var_4 = round(var_4)
print(f"Valoarea rotunjita a numarului {valoare} cu tip {type(valoare)} este {var_4}")
# De ce valorile cu .5 sunt rotunjite in minus?

print("-"*70)

# 5 ------------------------------
varsta = 15
inaltime = 1.88
nume = "Ion"
e_adolescent = True
job = "Aviator"
print(f"Numele meu este {nume} am {varsta} ani.")
print(f"Am inaltimea de {inaltime}")
print(f"Sunt adolescent = {e_adolescent}")
print(f"Jobul meu este de {job}")

print("-"*70)

# 6 ------------------------------
nume = input("Introdu numele:\n")
prenume = input("Introdu prenumele:\n")
nrcaract = len(nume)+len(prenume)
print(f"Numele complet are {nrcaract} caractere")
print("-"*70)

# 7 ------------------------------

latime = int(input("Afiseaza latimea: "))
lungime = int(input("Afiseaza lungimea"))
aria = latime * lungime
print(f"Aria dreptunghiului este: {aria}")

print("-"*70)

# 8 ------------------------------
sentence = "Coral is either the stupidest animal or the smartest rock"
print(f"In expresia {sentence}, cuvantul ''the'' apare de  {sentence.count('the')} ori")

print("-"*70)

# 9 ------------------------------
exemplu = 'Coral is either the stupidest animal or the smartest rock'
print(f'Cuvantul "the" apare de {exemplu.count("the")} ori')

print("-"*70)

# 10 ------------------------------

print("-"*70)

# 11 ------------------------------

print("-"*70)

# 12 ------------------------------

print("-"*70)

# 13 ------------------------------
tastatura = input("Scrie un string ")
print(tastatura)
x = tastatura[0]
y = tastatura.replace(x,x.upper())
print(y)
print(y[0].replace(y[0],y[0].lower())+y[1:-1]+y[-1].replace(y[-1],y[-1].lower()))
print("-"*70)

# 14 ------------------------------
user = input("Introduceti un user: ")
parola = input("Introduceti o parola: ")
lungime_parola = len(parola)
indicator = '*' * lungime_parola
print(f"Parola pt userul {user} este {indicator} și are {lungime_parola} caractere.") #varianta 1
print(f"Parola pt userul {user} este {'*' * len(parola)} și are {len(parola)} caractere.") #varianta 2
print(f"Parola pt userul {user} este {parola.replace(parola, '*' * len(parola))} si are {len(parola)} caractere.") #varianta 3
print(parola)