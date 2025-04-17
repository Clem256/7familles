from ListeCarte import *


class ListeMain:

    def __init__(self, listecartes: ListeCarte): #Johann
        """"
        Initialise la ListeMain avec une liste  et une ListeCarte donné
        :param listecartes:  ListeCarte pour initialiser la liste
        """
        self.premier = None
        self.dernier = None
        self.listecartes = listecartes
        self._nbElem = 0
        self._suiv = None

    def ajouter_main(self, main: ListeCarte): #Johann
        """
        Ajoute un nouvel objet ListeCarte à la liste.
        :param main: Objet ListeCarte à ajouter à la liste.
        """
        nouveau_maillon = main
        if self.premier == None:
            self.premier = nouveau_maillon
            self.dernier = nouveau_maillon
        else:
            self.dernier._suiv = nouveau_maillon
            self.dernier = nouveau_maillon
        self._nbElem += 1

    def suppr_main(self, p): #Johann
        """
        Supprime l'objet ListeCarte à la position p.
        :param p: Position de la ListeCarte à supprimer.
        :return: None
        """
        if p < 1 or p > self._nbElem or self.premier == None:
            return None
        prec = None
        cour = self.premier
        pos = 1
        while cour is not None and pos < p:
            prec = cour
            cour = cour._suiv
            pos += 1
        if prec is None:
            self.premier = cour._suiv
        else:
            prec._suiv = cour._suiv
        if cour == self.dernier:
            self.dernier = prec
        self._nbElem -= 1

    def taille_liste_mains(self): #Johann
        """
        Renvoie la taille de la ListeMain
        :return: nbElem
        """
        return self._nbElem

    def parcourir_jusqua(self, indice): #Johann
        """
        Parcours la liste jusqu'a l'indice
        : param indice : indice pour savoir jusqu'à ou on doit continuer
        :return: ListeCarte à l'indice donné ou None
        """
        cour = self.premier
        pos = 1
        while cour is not None and pos < indice:
            cour = cour._suiv
            pos += 1
        return cour
