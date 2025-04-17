from Carte import Carte
from chaines_pareilles import chaines_pareilles


class ListeCarte:
    def __init__(self): #Clement
        self.premier = None
        self.dernier = None
        self._nbElem = 0

    def retourner_pos(self, x): #Clement
        cour = self.premier
        i = 1
        while cour != None:
            if cour.get_famille() == x:
                return i
            cour = cour._suiv
            i = i + 1
        return None

    def ajouter_carte(self, carte: Carte): #Clement
        assert carte != None
        nouveau_maillon = carte
        if self.premier == None:
            self.premier = nouveau_maillon
            self.dernier = nouveau_maillon
        else:
            self.dernier._suiv = nouveau_maillon
            self.dernier = nouveau_maillon
        self._nbElem += 1

    def suppr_carte(self, p): #Clement
        if p < 1 or p > self._nbElem or self.premier == None:  # pos incorrect ou liste vide
            return None
        prec = None
        cour = self.premier
        pos = 1
        while cour != None and pos < p:
            prec = cour
            cour = cour._suiv
            pos += 1
        valsupp = cour.get_famille().get_nom()
        if prec == None:
            self.premier = cour._suiv
        else:
            prec._suiv = cour._suiv
        if cour == self.dernier:
            self.dernier = prec
        self._nbElem -= 1
        return valsupp

    def set(self, p, nouvVal): #Clement
        cour = self.premier
        pos = 1
        while cour != None and pos < p:
            cour = cour._suiv
            pos += 1
        if cour != None:
            cour.valeur = nouvVal

    def taille(self): #Clement
        return self._nbElem

    def parcourir_jusqua(self, indice): #Clement
        assert indice >= 0 and indice <= self._nbElem
        cour = self.premier
        pos = 1
        while cour != None and pos < indice:
            cour = cour._suiv
            pos += 1
        return cour if pos == indice else None

    def __contains__(self, carte: Carte): #Clement
        cour = self.premier
        trouve = False
        while cour is not None and not trouve:
            if chaines_pareilles(cour.get_famille().get_nom(), carte.get_famille().get_nom()):
                if chaines_pareilles(cour.get_membre(), carte.get_membre()):
                    trouve = True
            cour = cour._suiv
        return trouve

    def suppr(self, carte: Carte): #Clement
        prec = None
        cour = self.premier
        while cour is not None and cour.get_famille().get_nom() != carte.get_famille().get_nom() and cour.get_membre() != carte.get_membre():
            prec = cour
            cour = cour._suiv
        if cour is None:
            return None  # Le joueur n'a pas été trouvé
        valsupp = cour
        if prec is None:
            self.premier = cour._suiv
        else:
            prec._suiv = cour._suiv
        if cour == self.dernier:
            self.dernier = prec
        self._nbElem -= 1
        return valsupp

    def contains_membre(self, famille: str, membre: str): #Clement
        cour = self.premier
        trouve = False
        while cour is not None and not trouve:
            if chaines_pareilles(cour.get_famille().get_nom(), famille):
                if chaines_pareilles(cour.get_membre(), membre):
                    trouve = True
                else:
                    cour = cour._suiv
            else:
                cour = cour._suiv
        return trouve