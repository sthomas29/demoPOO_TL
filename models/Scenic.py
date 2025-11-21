from models.Voiture import Voiture


class Scenic(Voiture) :

    # Constructeur de Scenic
    def __init__(self, marque, modele, option):

        # Je fais appel au constructeur de la classe 'parent' (Voiture)
        super().__init__(marque, modele)

        # Un attribut spécifique de scenic
        self.__option=option

    def liste_options(self):
        print(self.__option)