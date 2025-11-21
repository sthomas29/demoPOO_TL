from models.Vehicule import Vehicule

class Voiture (Vehicule) :

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

    @kilometrage.setter
    def kilometrage(self, kilometrage) :
        if not isinstance(kilometrage, int) :
            raise TypeError("Kilométrage doit être un entier") # Exception (erreur maitrisée)

        if kilometrage <= self.__kilometrage :
            raise ValueError(f"Impossible de réduire le kilométrage à {kilometrage}") # Exception (erreur maitrisée)
        else:
            self.__kilometrage = kilometrage

    def rouler(self, kilometrage) :
        """
            Le code commenté ci-dessous est supprimable, car ces contrôles sont déjà réalisés
            dans la méthode 'self.kilometrage exécutée L56
        """
        #if not isinstance(kilometrage, int) :
        #    raise TypeError("Kilométrage doit être un entier") # Exception (erreur maitrisée)

        #if kilometrage <= 0 :
        #    raise ValueError(f"Impossible de réduire le kilométrage à {kilometrage}") # Exception (erreur maitrisée)

        #self.__kilometrage = self.__kilometrage + kilometrage

        self.kilometrage= self.__kilometrage + kilometrage

    def freiner(self):
        pass

    def arreter(self):
        pass

    def partir_en_vacances(self):
        print("Partir en vacances en famille en VOITURE !")


    # Redéfinir la fonction __str__() pour la classe Voiture
    def __str__(self) :
        return str(f"Voiture : {self.__marque} - {self.__modele} - {self.__kilometrage}")



"""
Caractéristiques ==> Attributs

Capacités ==> Méthodes (fonctions du langage)
"""