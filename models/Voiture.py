class Voiture :

    """
    self représente l'instance de voiture manipulée dans le script.py

    On utilise self uniquement dans la classe.
    """

    # Constructeur de Voiture
    def __init__(self, marque, modele, kilometrage=0) :
        self.__modele = modele
        self.__marque = marque
        self.__kilometrage = kilometrage

        print("Je crée une instance de voiture.")




    # Redéfinir la fonction __str__() pour la classe Voiture
    def __str__(self) :
        return str(f"Voiture : {self.__marque} - {self.__modele} - {self.__kilometrage}")



"""
Caractéristiques ==> Attributs

Capacités ==> Méthodes (fonctions du langage)
"""