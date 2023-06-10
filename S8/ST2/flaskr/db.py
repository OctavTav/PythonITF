"""
Aici tinem tot codul necesar pentru lucrul cu baza de date:
- initializare
- conexiune
- creare tabele
- in viitor, aici ar fi bine sa punem
"""

import sqlite3      # engine db care vine instalat cu Python, foarte lightweight, potrivit pentru development


import click        # librarie care ne ajuta sa cream comenzi de terminal
# current_app -> o referinta (un obiect) catre aplicatia curenta
# g -> un obiect special (global) care poate tine informatii intr-un ciclu req - res


from flask import current_app, g


def get_db():
    # punem db (conexiunea) pe g (global) pentru ca uneori pt o singura ruta vom aveanevoie sa apelam mai multe functii
    # si nu are sens ca la fiecare functie sa cerem o noua conexiunea (dpdv al performantei)
    if 'db' not in g:
        # aici ne conectam la DB
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# aici inchidem conexiunea la baza de date
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# aici citim din fisierul 'schema.sql' si executam instructiunile de acolo, pt a genera structura db
def init_db():
    db = get_db()   # obtinem o conexiunea

    # context manager care citeste un fisier
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# aici generam o comanda de terminal care se poate rula din flask
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


# init_db_command()
"""
Daca incercam sa apelam aceste fucntii fara contextul aplicatiei vom primi o eroare de runtime
"""
