"""
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nașterii
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat,
folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""


def visual_separator(func):
    def wrapper(*args, **kwargs):
        print('-' * 40)
        result = func(*args, **kwargs)
        print('-' * 40)
        return result
    return wrapper


def require_login(func):
    def wrapper(*args, **kwargs):
        print(f'Verificare login')
        logged, dict_info = func(*args, **kwargs)
        if logged:
            print('Account info:')
            print('-' * 40)
            for key, value in dict_info.items():
                print(f'{key} is {value}')
        else:
            print('Sorry, the user is not logged in!')

    return wrapper


class User:
    def __init__(self, u_name, u_email, u_pwd, u_birth_date):
        self.u_name = u_name
        self.u_email = u_email
        self.u_pwd = u_pwd
        self.u_birth_date = u_birth_date
        self.is_logged = False
        self.info_user = {'Name': self.u_name,
                          'Email': self.u_email,
                          'Password': self.u_pwd,
                          'Birth Date': self.u_birth_date}

    @visual_separator
    def login(self, email, pwd):
        if email == self.u_email and pwd == self.u_pwd:
            self.is_logged = True
            print('User logged in!')
        else:
            print('Email or password is wrong!')

    @visual_separator
    def logout(self):
        self.is_logged = False
        print('User logged out!')

    @visual_separator
    @require_login
    def get_info(self):
        return self.is_logged, self.info_user


u1 = User('asd', 'asdasd', '123', '01/Jan/1901')
u1.get_info()
u1.login('asdasd', '123')
u1.get_info()
u1.logout()
u1.get_info()
