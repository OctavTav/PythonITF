"""
HTTP - methods = ii zic serverului ce actiune sa faca cu resursa respectiva
Metodele HTTP sunt echivalente cu metodele de la bazele de date (CRUD = create, read, update, delete)

GET (read) - ia date de la server
POST (create) - creaza resurse noi pe server: de obicei, folosim metoda POST in REST APIs pe URL-ul general al
    resurseo : POST / products (deoarece atunci cand facem o resurse de obicei nu avem un id, serverul il genereaza
PUT/PATCH (update) : aceste metode ofera optiunea de a updata o anumita resursam ceea ce inseamna ca
    de obicei actioneaza pe un URL de genul /products.1
    - diferenta dintre ele este ca PUT face update la tot obiectul,
    in timp ce PATCH (partial update) updateaza doar campurile pe care le trimitem noi
DELETE (delete) : sterge o anumita resursa, din nou actioneaza pe /products/1

Dintre acestea, unele metode au nevoie sa trimitem si date catre server (POST, PUT, PATCH);
facem acest lucru folosind requests body (corpul request-ului).

"""

"""
STATUS CODES - returnate de server pt a stii statusul unui request
Exista 5 clase de status codes:
1XX (100 - 199) - INFO (informative)
2XX (200 - 299) - SUCCES (status codes de succes, cele mai importante sunt:
    200 - OK
    201 - CREATED
    204 - NO CONTENT
3XX (300 - 399) - REDIRECT (acestea ii zic clientului ca resursa cautata nu se mai gaseste la URL specificat
    si sa mearga sa caute in alta locatie
    304 - NOT MODIFIED (acest status code se foloseste pentru sistemul de caching)
4XX (400 - 499) - CLIENT ERROR (acestae sunt status=uri de eoare de client, adica clientul a gresit ceva
    iar serverul nu poate sa dea un raspuns bun
    400 - BAD REQUEST - atunci cand TRIMITEM niste date nepotrivite la server
    401 - UNAUTHORIZED - atunci cand clientul nu este logat
    403 - FORBIDDEN - atunci cand clientul este logat, dar nu are permisiuni sa faca o anumita actiune
    404 - NOT FOUND - atunci cand URL respectiv nu exista pe server
    405 - METHOD NOT FOUND
5XX (500 - 599) - SERVER ERROR (erori care apar pe server si nu sunt din cauza clientului)
    500 - INTERNAL SERVER ERROR - generic status code, si inseamna ca a aparut o eroare in codul de pe server
        care nu a fost gestionata (cu mecanismul de try-except)
    502 - BAD GATEWAY
    503 = SERVICE UNAVAILABLE
"""

"""
Pentru a lucra cu un API REST, instalam o librarie python numita requests:
pip install request
SAU
pip install -r requirements.txt - pentru proiectul luat cu pull de pe github
"""

import requests

BASE_URL = 'https://dummyjson.com'


"""
1. GET all products
"""
# response = requests.get(f"{BASE_URL}/products")
#
# print(f"Status code: {response.status_code}")
# if response.status_code == 200:
#     response_json = response.json()
#     # print(response_json)
#     # response_json, va fi un dictionar, deci il putem parcurge cu un for  key, value
#     print(f"Afisare {response_json['limit']} din {response_json['total']} produse")
#     print('-' * 40)
#     print(f"{'ID':^10}{'Title':^30}{'Price':^10}{'Category':^25}")
#     for product in response_json['products']:
#         product_id = product['id']
#         product_title = product['title']
#         product_price = product['price']
#         product_category = product['category']
#         print(f"{product_id:^10}{product_title:<40}{product_price:^10}{product_category:^25}")


"""
2. POST a new product
"""
# request_body = {
#     'title': 'Carte de programare in IT',
#     'price': 129,
#     'category': 'home-decoration',
#     'stock': 100
# }
# response = requests.post(f"{BASE_URL}/products/add", data = request_body)
# print(f"Status code: {response.status_code}")
# if response.status_code == 200 or response.status_code == 201:
#     product = response.json()
#     product_id = product['id']
#     print(f"S-a creat produsul cu ID-ul {product_id}")


"""
3. PUT = update a product
"""
# request_body = {
#     "title": "Samsung Galaxy 9",
#     "description": "Samsung's new variant which goes beyond Galaxy to the Universe",
#     "price": 1849
# }
# r1 = requests.get(f"{BASE_URL}/products/3")
# initial_product = r1.json()
#
# r2 = requests.put(f"{BASE_URL}/products/3", data=request_body)
# modified_product = r2.json()
#
# print(f"{'Column':^20}{'Before':^30}{'After':^30}")
#
# for key in ['id', 'title', 'price', 'stock', 'rating', 'brand', 'category']:
#     initial_val = initial_product[key]
#     modified_val = modified_product[key]
#     print(f'{key:^20}{initial_val:^30}{modified_val:^30}')


"""
4. DELETE - stergem un produs
"""

response = requests.delete(f'{BASE_URL}/products/19')
print(f'Status code: {response.status_code}')

product = response.json()
if product['isDeleted']:
    deleted_at = product['deletedOn']
    print(f'Deletion datetime: {deleted_at}')