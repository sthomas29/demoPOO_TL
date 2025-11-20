from models.Voiture import Voiture

entier = 40

chaine = "Toto"

""" 
clio est une instance de la classe 'Voiture'
"""
clio = Voiture("Renault","Clio")

#clio.__marque="Peugeot"

print(clio)

print(clio.get_marque())
print(clio.get_modele())
print(clio.get_kilometrage())

clio.set_kilometrage(50)

print(clio.get_kilometrage())
