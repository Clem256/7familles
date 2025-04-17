class Famille:
    def __init__(self, nom, compte): #Clement
        """
        Initialise une famille avec un nom et un compte
        :param nom: Nom de la famille.
        :param compte: nombre de fois qu'une famille est dans une main
        """
        self.nom=nom
        self.compte=compte

    def get_nom(self): #Clement
        """
        Retourne le nom de la famille
        :return: Nom de la famille
        """
        return self.nom
    
    def get_compte(self): #Clement
        """
        Retourne le compte de la famille
        :return: nombre de fois qu'une famille est dans une main
        """
        return self.compte
    
    def incr_compte(self): #Clement
        """
        Incrémente le compte de la famille.
        """
        self.compte+=1