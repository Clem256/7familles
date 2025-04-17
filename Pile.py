class Pile:
    class Maillon:  #Johann
        def __init__(self, val):
            self.suiv=None
            self.val=val

    def __init__(self): #Johann
        self.sommet=None
        
    def empiler(self, e): #Johann
        nouv_maillon=Pile.Maillon(e)
        nouv_maillon.suiv=self.sommet
        self.sommet=nouv_maillon

    def depiler(self): #Johann
        if self.est_vide():
            return None  # Rien à dépiler
        carteasuppr=self.sommet
        self.sommet=self.sommet.suiv
        return carteasuppr.val
        
    def get_sommet(self): #Johann
        if self.est_vide():
            return None  #si pile vide
        return self.sommet.val

    def est_vide(self): #Johann
        return self.sommet.val is None or self.sommet==None

    def vider(self): #Clement
        self.sommet = None

    def taille(self): #Clement
        taille=0
        cour=self.sommet
        while cour!=None:
            cour=cour.suiv
            taille+=1
        return taille

    def parcourir_jusqua(self, valeur): #Clement
        cour = self.sommet
        while cour is not None:
            if cour.val == valeur:
                return True
            cour = cour.suiv
        return False

