class File:

    class MaillonDouble: 

        def __init__(self, val):  #Clement
            self.suiv=None
            self.prec=None
            self.val=val


    def __init__(self): #Clement
        self.tete=None
        self.queue=None

    def enfiler(self, e): #Clement
        nouv_maillon=File.MaillonDouble(e)
        if self.est_vide():
            self.tete=nouv_maillon
            self.queue=nouv_maillon
        else:
            self.queue.suiv=nouv_maillon
            nouv_maillon.prec=self.queue
            self.queue=nouv_maillon

    def defiler(self): #Clement
        if self.est_vide():
            return None
        ancienne_tete=self.tete
        self.tete=self.tete.suiv
        if self.tete!=None:
            self.tete.prec=None#si tete non null alors pas de precedent car c la tete
        else:
            self.queue=None #si la tete est vide alors la queue aussi et donc la file aussi
        return ancienne_tete

    def est_vide(self): #Clement
        return self.tete==None or self.tete.val==None

    def vider(self): #Clement
        self.tete = None
        self.queue = None

    def get_tete(self): #Clement
        if self.est_vide():
            return None
        return self.tete

    def taille(self): #Clement
        cour=self.tete
        taille=0
        while cour!=None:
            cour=cour.suiv
            taille+=1
        return taille
    
    def __contains__(self,val): #Clement
        cour=self.tete
        trouve=False
        while cour!=None and not trouve:
            if cour.val==val:
                trouve=True
            cour=cour.suiv
        return trouve