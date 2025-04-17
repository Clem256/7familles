from ListeCarte import ListeCarte

class Joueur:
    def __init__(self, nom, main:ListeCarte): #Johann
        """
        Initialise un joueur avec un nom et une main
        :param nom: Nom du joueur
        :param main:  ListeCarte qui est la main du joueur
        """
        self.nom=nom
        self.main=main
        self.famille_completee=0
        self._suiv=None
        self.prec=None

    def get_nom(self): #Johann
        """
        Retourne le nom du joueur.
        :return: Nom du joueur
        """
        return self.nom
    
    def get_main(self): #Johann
        """
        Retourne la main de cartes du joueur
        :return:  ListeCarte qui est la main du joueur.
        """
        return self.main
    
    def incremente_nbfamille(self): #Johann
        """
        Incrémente le nombre de familles complétées
        """
        self.famille_completee+=1

    def get_nbfamcomp(self): # Johann
        """
        Retourne le nombre de familles complétées
        :return: Nombre de familles complétées
        """
        return self.famille_completee