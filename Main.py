from Carte import Carte
from ListeChainee import ListeChainee

class Main:
    def __init__(self): #Clement
        """
        Initialise la Main avec une listeChainee
        """
        self.cartes=ListeChainee()

    def ajouter_carte(self, carte:Carte): #Clement
        """
        Ajoute une carte à la main
        :param carte:  Carte à ajouter à la main
        """
        self.cartes.ajout(carte)

    def retirer_carte(self, carte): #Clement
        """
        Retire une carte de la main
        :param carte:  Carte à retirer
        """
        self.cartes.suppr(carte)

    def compter_cartes(self): #Clement
        """
        Compte le nombre de carte présent dans la main , c'est à dire la taille de la main
        :return: Nombre de carte
        """
        return self.cartes.taille
    
    
