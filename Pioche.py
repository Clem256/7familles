from Carte import  Carte

class Pioche:
    def __init__(self): #Clement
        """
        Initialise la pioche
        """
        self.sommet=None
        
    def empiler(self, carte:Carte): #Clement
        """
        Empile une carte en haut de la pioche
        :param carte:  Carte à empiler
        """
        nouv_maillon=Carte(carte.get_famille(), carte.get_membre())
        nouv_maillon.suiv=self.sommet
        self.sommet=nouv_maillon

    def depiler(self): #Clement
        """
        Dépile la carte du sommet de la pioche
        :return:  Carte dépilé ou None si la pioche est vide
        """
        if self.est_vide():
            return None  # Rien à dépiler
        carteasuppr=self.sommet
        self.sommet=self.sommet.suiv
        return carteasuppr
        
    def get_sommet(self): #Clement
        """
        Retourne la famille de la carte au sommet de la pioche
        :return: Famille de la carte au sommet ou None si la pioche est vide
        """
        if self.est_vide():
            return None  #si pile vide
        return self.sommet.get_famille()

    def est_vide(self): #Clement
        """
        Vérifie si la pioche est vide
        :return: True si la pioche est vide, sinon False
        """
        return self.sommet==None

    def taille(self): #Clement
        """
        Retourne le nombre de carte dans la pioche (ou taille de la pioche)
        :return: Nombre carte dans la pioche
        """
        taille=0
        cour=self.sommet
        while cour!=None:
            cour=cour.suiv
            taille+=1
        return taille