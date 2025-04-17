from Joueur import Joueur
class ListeJoueur:

    def __init__(self): #Clement
        """
        Initialise la Liste des joueurs
        """
        self.premier = None
        self.dernier = None
        self._nbElem = 0 
        
    def retourner_pos(self, x): #Clement
        """
        Retourne la position du joueur en fonction de x
        :param x: nom du joueur
        :return:Position du joueur ou None si pas trouvé
        """
        cour = self.premier 
        i = 1 
        while cour != None: 
            if cour.nom==x:
                return i
            cour = cour._suiv 
            i = i+1 
        return None

    def ajouter_joueur(self, joueur:Joueur): #Clement
        """
        Ajoute un nouveau joueur
        :param joueur: joueur a rajouter
        """
        if self.premier == None: 
            self.premier = joueur
            self.dernier = joueur
        else: 
            self.dernier._suiv = joueur
            self.dernier = joueur
        self._nbElem += 1


    def suppr_joueur(self,p): #Clement
        """
        Supprime un joueur qui est à la position p
        :param p: Position du joueur
        :return: Nom du joueur supprimée ou None si la position est incorrect
        """
        if p < 1 or p > self._nbElem or self.premier == None:  # pos incorrect ou liste vide
            return None
        prec=None
        cour=self.premier
        pos=1
        while cour!=None and pos<p:
            prec=cour
            cour=cour._suiv
            pos+=1
        valsupp=cour.nom
        if prec==None:
            self.premier=cour._suiv
        else:
            prec._suiv=cour._suiv
        if cour==self.dernier:
            self.dernier=prec
        self._nbElem-=1
        return valsupp

    def set(self,p,nouvVal): #Clement
        """
        Change le nom du joueur à la position p
        :param p: Position du joueur
        :param nouvVal: Nouveau nom
        """
        cour=self.premier
        pos=1
        while cour!=None and pos<p:
            cour=cour._suiv
            pos+=1
        if cour!=None:
            cour.nom=nouvVal
        
    def taille(self): #Clement
        """
        Renvoie la taille de la ListeJoueur
        :return: Nombre d'élément de ListeJoueur
        """
        return self._nbElem

    def parcourir_jusqua(self, indice): #Clement
        """
        Parcourt la ListeJoueur jusqu'à l'indice
        : param indice : indice pour savoir jusqu'à ou on doit continuer
        :return: Le joueur à la position indice ou None si l'indice est incorrect
        """
        cour=self.premier
        pos=1
        while cour!=None and pos<indice:
            cour=cour._suiv
            pos+=1
        return cour
    

    def __contains__(self, val): #Clement
        """
        Vérifie si un joueur avec le nom val est dans la liste
        :param val: Nom du joueur
        :return: True si le joueur est trouvé, sinon False
        """
        cour=self.premier
        trouve=False
        while cour!=None and not trouve:
            if cour.nom==val:
                trouve=True
            cour=cour._suiv
        return trouve
    
    def suppr(self, joueur: Joueur): #Clement
        """
        Supprime le Joueur donné
        :param joueur: Joueur à supprimer
        :return: Joueur supprimé ou None si le joueur n'a pas été trouvé
        """
        prec = None
        cour = self.premier
        while cour is not None and cour.get_nom() != joueur.get_nom():
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