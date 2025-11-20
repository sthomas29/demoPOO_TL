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

    """
        Accesseur via le décorateur @property
    """

    @property
    def modele(self):
        return self.__modele

    @property
    def marque(self):
        return self.__marque

    @property
    def kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage) :
        self.__kilometrage = kilometrage

    # Redéfinir la fonction __str__() pour la classe Voiture
    def __str__(self) :
        return str(f"Voiture : {self.__marque} - {self.__modele} - {self.__kilometrage}")



"""
Caractéristiques ==> Attributs

Capacités ==> Méthodes (fonctions du langage)
"""