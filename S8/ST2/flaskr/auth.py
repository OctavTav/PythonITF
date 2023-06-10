"""
Modulul de auth contine endpoint-uri precum:
- login
- login
- register

Ar mai putea contine
- forgot pass
- reset pass
- change user info
"""

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db


"""
In Flask, un BP (blueprint) este practic o colectie de rute, care ne permite sa grupam
aceste rute bazat pe functionalitatile lor. De exemplu aici vom avea un prefix pt toate rutele:
- /auth/login
- /auth/logout
- /auth/register
"""
bp = Blueprint('auth', __name__, url_prefix='/auth')


# aici nu vom mai avea @app.route, deoarece folosim un blueprint
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # trebuie sa cream un nou user
        # cu request.form luam datele primite in corpul requestului
        username = request.form['username']
        password = request.form['password']
        # obtinem apoi o conexiunea la baza de date
        db = get_db()
        # folosim o variabila numita error in care vom tine eventualele erori la inregistrare
        error = None

        # aici incepem sa facem validari:
        # 1. verificam daca campul de username a fost completat
        if not username:
            error = 'Username is required.'
        # 2.  Verificam daca campul de parola a fost completat
        elif not password:
            error = 'Password is required.'

        # Daca nu avem nici o eraoare dupa validari
        if error is None:
            # incercam sa introducem userul in baza de date
            # folosim un try-except deoarece avem o constragere (username este UNIC)
            try:
                # parolele nu se tin NICIODATA in baza de date in forma originala, ci DOAR criptate
                hashed_pass = generate_password_hash(password)
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, hashed_pass),
                )
                # commit (sql) reprezinta actiunea de permanentizarea a instructiunilor anteriaore
                # necesara pentru instructiuni care modifica datele din db
                db.commit()
            except db.IntegrityError:
                # avem constragere unica pe username, asa ca vom returna un mesaj de eroare
                # daca se incearca duplicarea acestuia
                error = f"User {username} is already registered."
            else:
                # try-except-else
                # else va fi apelat doar atunci cand try a fost exectutat cu succes
                return redirect(url_for("auth.login"))

        # daca am ajuns pana aici, inseamna ca avem o eroare la register,
        # si trebuie sa i-o afisam utilizatorului folosind functia flash (din flask)
        flash(error)

    # aici vom ajunge daca metoda nostra este GET, adica atunci cand utilizatorul vrea sa "ia: pagina de register
    # folosim functia de render templare care va randa un template HTML din folderul auth, numit register.html
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')


@bp.route('/base')
def base():
    pass
