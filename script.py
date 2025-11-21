from models.Scenic import Scenic
from models.Vehicule import Vehicule
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

clio.rouler(200)
print(clio)

clio.rouler(250)
print(clio)

scenic = Scenic("Renault", "Scenic", "Coffre de toit")

print(type(scenic))

print(scenic)
#scenic.__str__()

scenic.rouler(25)

print(scenic)
#scenic.liste_options()

scenic.partir_en_vacances()
