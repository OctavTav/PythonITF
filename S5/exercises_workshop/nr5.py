"""
Implementați următorii decoratori:
-	timeit – decorator care măsoară timpul de execuție al unei funcții
-	logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții

"""

import time


def logger(functie):
    def wrapper(*args, **kwargs):
        print(f'Date de intrare args {args}')
        print(f'Date de inrare kargs {kwargs}')
        request_logger = functie(*args, **kwargs)
        print(f'Date de iesire {request_logger}')
        return request_logger
    return wrapper


def timeit(functie):
    def wrapper(*args, **kwargs):
        print(f'Preprocesare')
        start_time = time.time()
        request_time = functie(*args, **kwargs)
        print(f'Postprocesare')
        print(f'Printam request_time: {request_time}')
        end_time = time.time()
        durata = end_time - start_time
        print(f'Durata de exectutie a functiei este {durata}')
        return request_time
    return wrapper


@timeit
def descrie_vreme(grade):
    print(f'Intram in descrie_vreme')
    time.sleep(5)
    return f'Vremea de afara este urata si are {grade} grade'


@timeit
def descrie_stare_spirit():
    time.sleep(3)
    return f'Starea de spirit este in parametrii optimi'


print(descrie_vreme(10))
# print(descrie_stare_spirit())


@logger
def mesaj(msg):
    print(f'Acesta este un mesaj text:\n {msg}')


# mesaj('A fost zarit in urs pe bulevardul turcilor')
