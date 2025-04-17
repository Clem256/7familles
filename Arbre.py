from Pile import Pile
from File import File


class Arbre:
    class Noeud: #Clement

        def __init__(self, value=0, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self, valeur):
        self.racine = Arbre.Noeud(valeur, None, None)

    def est_vide(self): # Johann
        return self.racine == None

    def recherche_noeud(self, noeud: Noeud): # Johann
        p = Pile()
        p.empiler(self.racine)
        trouve = False
        while not p.est_vide() or not trouve:
            courant = p.get_sommet()
            p.depiler()
            if courant.value == noeud.value:
                trouve = True
            else:
                if courant.right != None:
                    p.empiler(courant.right)
                if courant.left != None:
                    p.empiler(courant.left)
        return trouve

    def retirer_noeud(self, n: Noeud): #Johann
        p = Pile()
        p.empiler(self.racine)
        trouve = False
        while not p.est_vide() or not trouve:
            courant = p.get_sommet()
            p.depiler()
            if courant.left == n or courant.right == n:
                courant.left = None
                trouve = True
            else:
                if courant.right != None:
                    p.empiler(courant.right)
                if courant.left != None:
                    p.empiler(courant.left)

    def ajouter_noeud(self, parent: Noeud, direction): #Johann
        p = Pile()
        p.empiler(self.racine)
        trouve = False
        while not p.est_vide() or not trouve:
            courant = p.get_sommet()
            p.depiler()
            if courant == parent:
                if direction == "left":
                    courant.left = Arbre.Noeud(None, None, None)
                if direction == "right":
                    courant.right = Arbre.Noeud(None, None, None)
                trouve = True
            else:
                if courant.right != None:
                    p.empiler(courant.right)
                if courant.left != None:
                    courant.empiler(courant.left)

    def parcours_prefixe(self): #Clement
        p = Pile()
        p.empiler(self.value)
        while not p.est_vide():
            n = p.get_sommet()
            p.depiler()
            print(n.val)
            if n.right != None:
                p.empiler(n.right)
            if n.left != None:
                p.empiler(n.left)

    def parcours_suffixe(self): #Clement
        p = Pile()
        p.empiler(self.value)
        while not p.est_vide():
            n = p.get_sommet()
            if n.right != None:
                p.empiler(n.right)
            if n.left != None:
                p.empiler(n.left)
            p.depiler()
            print(n.val)

    def parcours_infixe(self): #Clement
        p = Pile()
        p.empiler(self.value)
        while not p.est_vide():
            n = p.get_sommet()
            if n.right != None:
                p.empiler(n.right)
            p.depiler()
            print(n.val)
            if n.left != None:
                p.empiler(n.left)

    def parcours_largeur(self): #Johann
        f = File()
        f.enfiler(self)
        while not f.est_vide():
            n = f.get_tete()
            f.defiler()
            print(n.val)
            if n.left != None:
                f.enfiler(n.left)
            if n.right != None:
                f.enfiler(n.right)

    def ParcoursPrefixe_recursif(self): #Clement
        if self is not None:
            print(self.value)
            if self.left:
                self.left.ParcoursPrefixe_recursif()
            if self.right:
                self.right.ParcoursPrefixe_recursif()

    def parcours_suffixe_recursif(self): #Clement
        if self is not None:
            if self.left:
                self.left.ParcoursPrefixe_recursif()
            if self.right:
                self.right.ParcoursPrefixe_recursif()
            print(self.value)

    def parcours_infixe_recursif(self): #Clement
        if self is not None:
            if self.left:
                self.left.ParcoursPrefixe_recursif()
            print(self.value)
            if self.right:
                self.right.ParcoursPrefixe_recursif()

    def taille_recursif(self): # Clement
        if not (self):
            return 0
        else:
            return 1 + self.taille_recursif(self.left) + self.taille_recursif(self.right)

    def hauteur_recursif(self): # Clement
        if not (self):
            return -1
        else:
            return 1 + max(self.hauteur_recursif(self.left), self.hauteur_recursif(self.right))

    def recherche_recursif(self, val): #Clement
        present = False
        if self.value == val:
            return True
        if self is None:
            return False
        return (self.recherche_recursif(self.right, val) or self.recherche_recursif(self.left, val))

    def recherche_min_recursif(self): #Clement
        if self == None:
            return 0
        else:
            return min(self.recherche_min_recursif(self.left), self.recherche_min_recursif(self.right))

    def ajouter(self, val): #Clement
        if self.value is None:
            self.value = val
        elif val < self.value:
            if self.left is None:
                self.left = Arbre(val)
            else:
                self.left.ajouter(val)
        else:
            if self.right is None:
                self.right = Arbre(val)
            else:
                self.right.ajouter(val)

    def nb_feuilles(self): #Johann
        feuilles = 0
        f = File()
        f.enfiler()
        while not f.est_vide():
            n = f.get_tete()
            f.defiler()
            if n.left != None:
                f.enfiler(n.left)
            if n.right != None:
                f.enfiler(n.right)
            if n.right is None and n.left is None:
                feuilles += 1
        return feuilles

    def parcourir_jusqua(self, val): #Clement
        if self is None:
            return False
        if self.value == val:
            return True
        if self.left and self.left.parcourir_jusqua(val):
            return True
        if self.right and self.right.parcourir_jusqua(val):
            return True
        return False

    def vider(self):
        self.racine = None
