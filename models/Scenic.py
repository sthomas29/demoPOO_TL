from models.Monospace import Monospace
from models.Voiture import Voiture


class Scenic(Monospace) :

    # Constructeur de Scenic
    def __init__(self, marque, modele, option):

        # Je fais appel au constructeur de la classe 'parent' (Voiture)
        super().__init__(marque, modele)

        # Un attribut spécifique de scenic
        self.__option=option

    def liste_options(self):
        print(self.__option)

    def rouler(self, kilometrage):
        print ("Je roule avec un scenic et son coffre de toit")
        super().rouler(kilometrage)

    def partir_en_vacances(self):
        print("Partir en vacances en famille en SCENIC - MONOSPACE - VOITURE !")

    def __str__(self):
        return f"Scenic - {super().__str__()} - {self.__option}"
