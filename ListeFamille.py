from Famille import Famille


class ListeFamille:

    def __init__(self): #Johann
        """
        Initialise la Liste des familles
        """
        self.premier = None
        self.dernier = None
        self._nbElem = 0

    def retourner_pos(self, x): #Johann
        """
        Retourne la position de la famille avec le nom x
        :param x: Nom de la famille
        :return: Position de la famille ou None si pas trouvée
        """
        cour = self.premier
        i = 1
        while cour != None:
            if cour.nom == x:
                return i
            cour = cour._suiv
            i = i + 1
        return None

    def ajouter_famille(self, famille: Famille): #Johann
        """
        Ajout d'une famille dans la ListeFamille
        :param famille: Famille à ajouter
        """
        nouveau_maillon = famille
        if self.premier is None:
            self.premier = nouveau_maillon
            self.dernier = nouveau_maillon
        else:
            self.dernier._suiv = nouveau_maillon
            self.dernier = nouveau_maillon
        self._nbElem += 1

    def suppr_famille(self, p): #Johann
        """
        Supprime la Famille à la position donnée
        :param p: Position de la famille
        :return: Nom de la famille si supprimé ou None
        """
        if p < 1 or p > self._nbElem or self.premier == None:  # pos incorrect ou liste vide
            return None
        prec = None
        cour = self.premier
        pos = 1
        while cour != None and pos < p:
            prec = cour
            cour = cour._suiv
            pos += 1
        valsupp = cour.nom
        if prec == None:
            self.premier = cour._suiv
        else:
            prec._suiv = cour._suiv
        if cour == self.dernier:
            self.dernier = prec
        self._nbElem -= 1
        return valsupp

    def set(self, p, nouvVal): #Johann
        """
        Modification du nom de la famille à la position donnée
        :param p: Position de la famille
        :param nouvVal: Position de la famille
        """
        cour = self.premier
        pos = 1
        while cour != None and pos < p:
            cour = cour._suiv
            pos += 1
        if cour != None:
            cour.nom = nouvVal

    def taille(self): #Johann
        """
        Retourne le nombre d'éléments de la ListeFamille
        :return: Nombre d'éléments
        """
        return self._nbElem

    def parcourir_jusqua(self, indice): #Johann
        """
        Parcourt la ListeFamille jusqu'à l'indice
        :param indice: indice pour savoir jusqu'à ou on doit continuer
        :return: Famille à l'indice donnée ou None si pas trouvée
        """
        cour = self.premier
        pos = 1
        while cour != None and pos < indice:
            cour = cour._suiv
            pos += 1
        return cour

    def __contains__(self, val): #Johann
        """
        Vérifie si une famille avec un nom est dans la liste
        :param val: Nom de la famille
        :return: True si la famille est trouvée sinon False
        """
        cour = self.premier
        trouve = False
        while cour is not None and not trouve:
            if cour.nom == val:
                trouve = True
            cour = cour._suiv
        return trouve

    def chercher_famille(self, famille): #Johann
        """
        Cherche une famille avec le nom en paramètre
        :param famille: Nom de la famille
        :return: La famille trouvé ou None sinon
        """
        cour = self.premier
        trouve = False
        while cour is not None and not trouve:
            if cour.nom == famille:
                trouve = True
                return cour
            cour = cour._suiv
        return None
