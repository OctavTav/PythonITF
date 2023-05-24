import requests

body = {
    'username': 'Octav',
    'password': 'helou'
}

auth_response = requests.post('https://dummyjson.com/auth/login', data=body)
print(f'Status code: {auth_response.status_code}')
print(auth_response.json())


body = {
    'username': 'atuny0',
    'password': '9uQFF1Lh'
}
auth_response = requests.post('https://dummyjson.com/auth/login', data=body)
print(f'Status code: {auth_response.status_code}')
print(auth_response.json())

"""
De obicei, atunci cand avem un request de lgin/auth, vom primi un token, care mai apoi trebuie
sa fie setat in headers pentru orice request-uri subsecvente, pentru ca serverul sa stie cine suntem noi
"""
correct_response = auth_response.json()
auth_token = correct_response['token']


"""
Header = metainformatii pe care serverul si clientul le schimba intre ei, pentru a stii cum sa comunice
Exemple de headers:
ACCEPT = clientul ii zice server-uli ce fel de formate stie sa accepte (json, xml,...)
AUTHORIZATION - header in care clientul poate trimite un token, astfel incat server-ul stie sa autorizeze
    un anumit request
EXPIRES - header trimis de server in care instiinteaza clientul in cat timp ii expira 'puterea' de 
    schimba valori 
LOCATION - server-ul ii zice clientului unde este locatia unei anumite resurse (de obicei pe status codes 3XX)

"""

headers = {
    'Authorization': f'Bearer {auth_token}'
}