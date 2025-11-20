from models.Voiture import Voiture

entier = 40

chaine = "Toto"

""" 
clio est une instance de la classe 'Voiture'
"""
clio = Voiture("Renault","Clio")

clio.__marque="Peugeot"

print(clio.__marque)

print(clio)