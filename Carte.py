from Famille import Famille

class Carte:
    def __init__(self, famille:Famille, valeur, dispo=True): # Johann
        """
        Initialise une carte avec une famille, une valeur et une disponibilité
        :param famille:  Famille qui est la famille de la carte
        :param valeur: Valeur de la carte
        :param dispo: Disponibilité de la carte (True par défaut)
        """
        self.famille = famille
        self.valeur = valeur
        self.dispo=dispo
        self._suiv=None

    def get_dispo(self): # Johann
        """
        Retourne la disponibilité de la carte
        :return: Disponibilité de la carte
        """
        return self.dispo
    
    def set_dispo(self, bool): # Johann
        """
        Modifie la disponibilité de la carte (passe de True vers False et de False vers True)
        :param bool: Nouvelle disponibilité de la carte
        """
        self.dispo=bool

    def get_famille(self): #Johann
        """
        Retourne la famille de la carte.
        :return:  Famille qui est la famille de la carte.
        """
        return self.famille
    
    def set_famille(self, nom): # Johann
        """
        Modifie le nom de la famille de la carte
        :param nom: Nouveau nom
        """
        self.famille.nom=nom
    
    def get_membre(self): # Johann
        """
        Retourne la valeur de la carte (qui est un membre de la famille)
        :return: Valeur de la carte
        """
        return self.valeur
