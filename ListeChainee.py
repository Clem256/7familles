
class ListeChainee:

    class Maillon:

        def __init__(self,val): #Johann
            self._suiv = None
            self._val = val

    def __init__(self): #Johann
        self.premier = None
        self.dernier = None
        self._nbElem = 0 
        
    def retourner_pos(self, x):  #Johann
        cour = self.premier 
        i = 1 
        while cour != None: 
            if cour._val==x:
                return i
            cour = cour._suiv 
            i = i+1 
        return None

    def ajout(self, x): #Johann
        nouveau_maillon = ListeChainee.Maillon(x)
        if self.premier is None:
            self.premier = nouveau_maillon
            self.dernier = nouveau_maillon
        else: 
            self.dernier._suiv = nouveau_maillon
            self.dernier = nouveau_maillon
        self._nbElem += 1

    def ajout_debut(self, x): #Johann
        nouveau_maillon = ListeChainee.Maillon(x)
        if self.premier is None:
            self.premier = nouveau_maillon
            self.dernier = nouveau_maillon
        else:
            nouveau_maillon._suiv = self.premier
            self.premier = nouveau_maillon
        self._nbElem += 1

    def suppr(self,p): #Johann
        if p < 1 or p > self._nbElem or self.premier == None:  # pos incorrect ou liste vide
            return None
        prec=None
        cour=self.premier
        pos=1
        while cour!=None and pos<p:
            prec=cour
            cour=cour._suiv
            pos+=1
        valsupp=cour._val
        if prec==None:
            self.premier=cour._suiv
        else:
            prec._suiv=cour._suiv
        if cour==self.dernier:
            self.dernier=prec
        self._nbElem-=1
        return valsupp

    def set(self,p,nouvVal): #Johann
        cour=self.premier
        pos=1
        while cour!=None and pos<p:
            cour=cour._suiv
            pos+=1
        if cour!=None:
            cour._val=nouvVal
        
    def taille(self): #Johann
        return self._nbElem

    def parcourir_jusqua(self, indice): #Johann
        cour=self.premier
        pos=1
        while cour!=None and pos<indice:
            cour=cour._suiv
            pos+=1
        return cour

    def trie(self): #Johann
        trier = False
        while trier == False:
            trier = True
            current = self.premier
            while current._suiv != None:
                suivant = current._suiv
                if current._val > suivant._val:
                    current._val, suivant._val = suivant._val, current._val
                    trier = False
                current = suivant

    def vider(self): #Johann
        self.premier = None
        self.dernier = None
        self._nbElem = 0

    def __contains__(self, val): #Johann
        cour=self.premier
        trouve=False
        while cour!=None and not trouve:
            if cour._val==val:
                trouve=True
            cour=cour._suiv
        return trouve