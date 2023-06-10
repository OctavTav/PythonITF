"""
1.	Write a SQL statement to create a table called continents, with the following columns:
a.	continent_id
b.	continent_name
c.	continent_code – 2 letters code, use this link

"""

import sqlite3

conexiune = sqlite3.connect('geografie.db')     # stabilim o conexiune cu baza de date ca sa putem interactiona cu ea
cursor = conexiune.cursor()     # ne ajuta sa interactionam in  baza de data cand avem mai multe queries
# cursor.execute('''
# CREATE TABLE continents(
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name TEXT NOT NULL,
#     continent_code CHAR(2) NOT NULL
#     );
#
# ''')

continente = [('Africa', 'AF'), ('North America', 'NA'), ('South America', 'SA'), ('Antarctica', 'AN'), ('Australia', 'OC'), ('Asia', 'AS'), ('Europe', 'EU')]
sql_query = 'INSERT INTO continents(continent_name, continent_code) VALUES(?,?)'
cursor.executemany(sql_query, continente)
conexiune.commit()  # ca sa se salveze modificarile aduse la baza de date

