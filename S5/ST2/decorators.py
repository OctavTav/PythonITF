""""
Decorators = functii speciale care ne permit sa augmentam alte functii
Putem face anumite actiuni folosin deoratorii atat inainte, cat si dupa apelarea functiei decorate
SIntaxa de folosire :
@decorator
def nume_functie_decorata(...):


Sintaxa de implementare:

def decorator_func(decorated_func):
    def inner_func(*args, **kwargs)
        #   actiuni inaintea functiei decorate
        decorated_func()
        #   actiuni dupa functia decorata

    return decorated_func
"""


def print_hi_and_bye(func):
    def inner_func():
        print("Hi")
        func()      # apelam functia originala
        print("Bye")
    return inner_func


@print_hi_and_bye
def say_hello():
    print("Hello, I am a function")


def introduce_yourself():
    print("Hi, my name is Adela")

say_hello()
introduce_yourself()

"""
De ce folosim decoratori? In general, pentru a adauga o anumita functionalitate in mai multe locuri.
Exemplu din Django -> decoratorul de login_required

principiul DRY = DON'T REPEAT YOURSELF

@login_required
def view_all_products():
    ---
"""
print("-" * 40)

"""
Pentru a decora functii cu parametrii, avem nevoie sa stim si de existenta parametrilor in decorator

"""


# def decadd(func):
#     def inner(x, y):    # aici avem nevoie de acelasi numar de param ca si un functia originala
#         print("Adding stuff...")
#         result = func(x, y)     # aici trebuie sa apelam functia originala cu parametrii primiti,
#                                 # si sa nu uitam sa returnam rezulatul la final
#         print("Done adding stuff")
#         return result
#     return inner


def decadd(func):
    def inner(*args, **kargs):    #
        print("Adding stuff...")
        print(f'Positional params: {args}')
        print(f'keyword params: {kargs}')
        result = func(*args, **kargs)
        print("Done adding stuff")
        return result
    return inner


@decadd
def add2(a, b):
    return a + b


@decadd
def add3(a, b, c):
    return a + b + c


@decadd
def add4(a, b, c=0, d=100):
    return a + b + c + d


print(add2(10, 17))
print(add3(1, 2, 4))
print(add4(1, 2, c=5))

"""
args = arguments, sau parametrii pozitionali ai unei functii. Atunci cand nu stim excat
 cati parametrii pozitionali va avea o functie, pasa *args, deoarece acei parametrii vor fi
 "impachetati" intr-o tupla numita args, iar folosind steluta, facem operatiunea de despachetare
 packing/unpacking
 
 kwargs = keyword arguments, adica parametrii NUMITI ai unei functii. Acestia sunt "impachetati"
 sub forma unui dictionar, si sunt despachetati folosind doua stelute
"""

"""
Sintaxa finala a unui decorator (care functioneaza cu orice tipuri de functii)

def decorator(func_originala):
    def inner(*args, **kwargs)
        ...preprocesare [optional]
        result = func_originala(*args, **kwargs)
        ...post-procesare [optional]
        return result
        
"""

"""
Putem avea mai  multi decoratori pentru aceeasi functie1
Chainin = inlantuire a decoratorilor, adica acestia se apeleaza pe rand

@dec1
@dec2
def func(...):
    ...
    
Apelarea unei functii decorate ar fi echivalent cu:
dec1 ( dec2 ( func() ))

@login_required
@user_is_admin
def view_products():
    ...

"""