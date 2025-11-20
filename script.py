from models.Voiture import Voiture

entier = 40

chaine = "Toto"

""" 
clio est une instance de la classe 'Voiture'
"""
clio = Voiture("Renault","Clio")

#clio.__marque="Peugeot"

print(clio)

print(clio.marque)
print(clio.kilometrage)

clio.kilometrage=100
print(clio.kilometrage)

clio.kilometrage=150

print(clio.kilometrage)

print(clio.modele)

print(clio)
