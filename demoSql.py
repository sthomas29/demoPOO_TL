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

def get_connection():
    conn = sqlite3.connect("demoBDD_TL.db")
    return conn

def execute_query(query, params=()):

    #print (f"Type : {type(params)}")

    print (f"Exécution requête : {query} - {params}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)

    result = cursor.fetchall()
    #print (f"Retour : {result}")

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

execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Minnie", 90))
execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Mickey", 95))
execute_query("INSERT INTO users (name, age) VALUES (?,?)", ("Donald",85))
execute_query("INSERT INTO users (name) VALUES (?)", ("Pluto",))
execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ("Picsou",85))
execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ("Picsou",85))

# R de CRUD (Lecture depuis lune BDD
print("--- R de CRUD ---")
resultat = execute_query("SELECT * FROM users")

for user in resultat:
    print(f"{user[1]} - {user[2]} ({user[0]})")



# ("Pluto") ==> Chaine de caractères, identique à "Pluto"
# ("Pluto",) ==> Tuple


# Requête générant une faille de sécurité (injection SQL)
#execute_query("INSERT INTO users (name, age) VALUES ('');DROP table users") #Minnie', 90)")


print("Fin script bdd")


# Transaction
""" Débit
    Controle de ma banque sur la solvabilité
    Connexion sur la banque de destination
    Vérification du compte bancaire de destination
    Vérification de l'indentité du destinateur
    Transfert de valeur (crédit) sur le compte destinataire

==> rollback() : retour arrière de toutes les étapes précédentes de la transaction
==> commit() : validation effective de toutes les transactions
"""



