#renvoie True si les deux chaines sont identiques, False sinon
def chaines_pareilles(chaine1:str, chaine2:str): #Johann
    if len(chaine1)!=len(chaine2):
        return False
    for i in range(len(chaine1)):
        if chaine1[i]!=chaine2[i]:
            return False
    return True