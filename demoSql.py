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

REQ_DROP_TABLE_USERS="DROP TABLE IF EXISTS users"
REQ_CREATE_USERS="""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        age INTEGER
                 )"""

REQ_SELECT_ALL="SELECT * FROM users"
REQ_SELECT_BY_NAME="SELECT * FROM users WHERE name = ?"
REQ_SELECT_BY_ID="SELECT * FROM users WHERE id = ?"
REQ_SELECT_BY_AGE="SELECT * FROM users WHERE age = ?"
REQ_UPDATE_AGE="UPDATE users SET age = ? WHERE name = ?"
REQ_DELETE_USER="DELETE FROM users WHERE name = ?"
REQ_INSERT_USER="INSERT INTO users (name, age) VALUES (?, ?)"
REQ_INSERT_USER_ONLY_NAME ="INSERT INTO users (name) VALUES (?)"

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

# Drop == Suppression de la table users si elle existe
execute_query(REQ_DROP_TABLE_USERS)

# Création de la table users si elle n'existe pas
execute_query(REQ_CREATE_USERS)

# C de CRUD (création d'un enregistrement dans la table)
print("--- C de CRUD ---")

execute_query(REQ_INSERT_USER, ("Minnie", get_age(1928,11,18)))
execute_query(REQ_INSERT_USER, ("Mickey", get_age(1928,11,18)))
execute_query(REQ_INSERT_USER, ("Donald", get_age(1934,6,9)))
execute_query(REQ_INSERT_USER_ONLY_NAME, ("Pluto",))
execute_query(REQ_INSERT_USER, ("Picsou",get_age(1867,7,8)))

# R de CRUD (Lecture depuis une BDD)
print("--- R de CRUD ---")
resultat = execute_query(REQ_SELECT_ALL)

# for user in resultat:
#     print(f"{user[1]} - {user[2]} ({user[0]})")

# U de CRUD
execute_query(REQ_UPDATE_AGE, (get_age(1930, 8,18),"Pluto"))

execute_query(REQ_SELECT_BY_NAME, ("Pluto",))

execute_query(REQ_INSERT_USER, ("Pat Hibulaire", get_age(1925,2,15)))
execute_query(REQ_SELECT_BY_NAME, ("Pat Hibulaire",))

# D de CRUD
execute_query(REQ_DELETE_USER, ("Pat Hibulaire",))
execute_query(REQ_SELECT_ALL)

print("Fin script bdd")
