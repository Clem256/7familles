from Joueur import Joueur

class Ordre:

    def __init__(self): #Johann
        """
        Initialise l'ordre avec une tete et une queue
        """
        self.tete=None
        self.queue=None

    def enfiler(self, joueur: Joueur): #Johann
        """
        Ajoute un joueur à la fin de l'ordre
        :param joueur:  Joueur à ajouter
        """
        nouv_maillon=joueur
        if self.est_vide():
            self.tete=nouv_maillon
            self.queue=nouv_maillon
        else:
            self.queue._suiv=nouv_maillon
            nouv_maillon.prec=self.queue
            self.queue=nouv_maillon

    def defiler(self): #Johann
        """
        Retire et retourne le joueur en première position de l'ordre
        :return:  Joueur retiré ou None si il n'y a pas d'ordre
        """
        if self.est_vide():
            return None
        ancienne_tete=self.tete
        self.tete=self.tete._suiv
        if self.tete!=None:
            self.tete.prec=None     #si tete non null alors pas de precedent car c la tete
        else:
            self.queue=None     #si la tete est vide alors la queue aussi et donc la file aussi
        return ancienne_tete

    def est_vide(self): #Johann
        """
        Vérifie si l'ordre est vide
        :return: True si vide, sinon False.
        """
        return self.tete==None
        
    def get_tete(self): #Johann
        """
        Retourne le joueur en tête
        :return:  Joueur en tête  ou None l'ordre est vide.
        """
        if self.est_vide():
            return None
        return self.tete

    def taille(self): #Johann
        """
        Retourne le nombre de joueurs
        :return: Nombre de joueurs
        """
        cour=self.tete
        taille=0
        while cour!=None:
            cour=cour._suiv
            taille+=1
        return taille
    
    def __contains__(self,val): #Johann
        """
        Vérifie si un joueur avec un nom donné est présent
        :param val: Nom du joueur à rechercher
        :return: True si le joueur est dedans, sinon False.
        """
        cour=self.tete
        trouve=False
        while cour!=None and not trouve:
            if cour.get_nom()==val:
                trouve=True
            cour=cour._suiv
        return trouve