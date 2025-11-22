""""
Application métier
    Python
    Java
    php
    C# (C sharp)
    Javascript

Application Base de Données :
    Mysql /Mariadb
    postgreSql
    oracle db
    MS Sql Server
    sqlite

"""

import sqlite3
from datetime import date


def get_connection():
    conn = sqlite3.connect("demoBDD_TL.db")
    return conn

def get_age(year,month,day):
    date_ref = date(year,month,day)  # exemple
    aujourdhui = date.today()

    age = aujourdhui.year - date_ref.year - (
        (aujourdhui.month, aujourdhui.day) < (date_ref.month, date_ref.day)
    )
    return age

def execute_query(query, params=()):

    #print (f"Type : {type(params)}")

    print (f"Exécution requête : {query} - {params}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)

    result = cursor.fetchall()
    #print (f"Retour : {result}")
    if result is not None:
        for user in result:
            print(f"{user[1]} - {user[2]} ({user[0]})")
        print()
    conn.commit()
    conn.close()

    return result

# Drop == Supression de la table users si elle existe
execute_query("DROP TABLE IF EXISTS users")

# Création de la table users si elle n'existe pas
execute_query("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        age INTEGER
                 )""")

# C de CRUD (création d'un enregistrement dans la table)
print("--- C de CRUD ---")

execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Minnie", get_age(1928,11,18)))
execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Mickey", get_age(1928,11,18)))
execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Donald", get_age(1934,6,9)))
execute_query("INSERT INTO users (name) VALUES (?)", ("Pluto",))
execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ("Picsou",get_age(1867,7,8)))

# R de CRUD (Lecture depuis une BDD)
print("--- R de CRUD ---")
resultat = execute_query("SELECT * FROM users")

# for user in resultat:
#     print(f"{user[1]} - {user[2]} ({user[0]})")

# U de CRUD
execute_query("UPDATE users SET age = ? WHERE name = ?", (get_age(1930, 8,18),"Pluto"))

execute_query("SELECT * FROM users WHERE name = ?", ("Pluto",))

execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Pat Hibulaire", get_age(1925,2,15)))
execute_query("SELECT * FROM users WHERE name = ?", ("Pat Hibulaire",))

# D de CRUD
execute_query("DELETE FROM users WHERE name = ?", ("Pat Hibulaire",))
execute_query("SELECT * FROM users")

print("Fin script bdd")
