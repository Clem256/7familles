from File import File
from Pile import Pile
from random import randint
from Joueur import Joueur
from Famille import Famille
from ListeFamille import ListeFamille
from ListeJoueur import ListeJoueur
from ListeMain import ListeMain
from ListeMain import *
from Ordre import Ordre
from Pioche import Pioche
from chaines_pareilles import chaines_pareilles
import time

membres = ["fils", "fille", "mère", "père", "grand-mère", "grand-père"]
fam = ["ParRabus", "Douze", "Zikette", "Donuts", "Pierrafeu", "Pirate", "Intolérants au lactose"]
familles = ListeFamille()
for nom in fam:
    familles.ajouter_famille(Famille(nom, 0))
familles2 = ["Ature", "MisdeConduire", "Sonnel", "Rit", "Pétuel", "Méable", "Tule"]
famillesIut = []
liste_cartes = ListeCarte()
for i in range(1, familles.taille() + 1):
    famille = familles.parcourir_jusqua(i)
    if famille is not None:
        for membre in membres:
            liste_cartes.ajouter_carte(Carte(famille, membre, True))
liste_joueurs = ListeJoueur()
liste_mains = ListeMain(None)  # on ne retire pas ce None ! sinon ça casse tout et Jojo -> pas content
pioche = Pioche()
ordre = Ordre()


# on lance le jeu ouuuuuu
def start_game():  # JOHANN
    # nbjoueurs=randint(2,5)
    nbfamilles_constituees = 0
    nbjoueurs = 2
    generer_pioche()
    generer_mains(nbjoueurs)

    i = 0
    while i < nbjoueurs:
        liste_joueurs.ajouter_joueur(Joueur(f"Joueur {i}", liste_mains.parcourir_jusqua(i)))
        i += 1

    init_ordre()

    while nbfamilles_constituees < 6:
        joueur_qui_joue = ordre.defiler()
        print(f"C'est au tour de {joueur_qui_joue.get_nom()} !")
        if joueur_qui_joue.get_main().premier is None:
            print(f"{joueur_qui_joue} n'a plus de carte, il pioche")
            piocher(joueur_qui_joue)
        else:
            carte_demandee = choisir_carte_demandee(joueur_qui_joue)
            print(
                f"{joueur_qui_joue.get_nom()} demande la carte {carte_demandee.get_membre()} de la famille {carte_demandee.get_famille().get_nom()}")
            demander_carte(joueur_qui_joue, carte_demandee)
        print(pioche.taille())
        for famille in fam:
            if possede_famille(joueur_qui_joue, famille):
                constituer_famille(famille, joueur_qui_joue)
                nbfamilles_constituees += 1
                joueur_qui_joue.incremente_nbfamille()
        print(nbfamilles_constituees)
        ordre.enfiler(joueur_qui_joue)

        # Add a sleep of 1 second between turns
        time.sleep(1)

    # fin de partie
    compte_max = 0
    joueur_gagnant = None
    for i in range(1, nbjoueurs):
        if liste_joueurs.parcourir_jusqua(i).get_nbfamcomp() > compte_max:
            joueur_gagnant = liste_joueurs.parcourir_jusqua(i)
            compte_max = liste_joueurs.parcourir_jusqua(i).get_nbfamcomp()
    print(f"Le joueur {joueur_gagnant.get_nom()} a complété le plus de familles !")
    print("Fin de la partie !")


# on remplit la pioche
def generer_pioche():  # Johann
    # Vérifiez la taille de la liste
    for i in range(1, liste_cartes.taille() + 1):
        carte = liste_cartes.parcourir_jusqua(i)
        if carte is not None:
            pioche.empiler(carte)


# distribution des cartes aux joueurs tu captes
def generer_mains(nbjoueurs: int):  # Johann
    # Vérification si la pioche contient suffisamment de cartes
    if pioche.taille() < nbjoueurs * 4:
        raise ValueError("La pioche ne contient pas assez de cartes pour distribuer des mains à tous les joueurs.")

    # Distribution des mains
    for i in range(nbjoueurs):
        main = ListeCarte()
        print("main du joueur ", i)
        for j in range(4):
            if not pioche.est_vide():  # Vérifiez si la pioche a encore des cartes
                carte_depilee = pioche.depiler()
                if carte_depilee is not None:
                    main.ajouter_carte(carte_depilee)
                    print(carte_depilee.get_famille().get_nom(), carte_depilee.get_membre())
        liste_mains.ajouter_main(main)


# initialise l'ordre de passage
def init_ordre():  # Johann
    for i in range(1, liste_joueurs.taille() + 1):
        joueur_enfile = liste_joueurs.parcourir_jusqua(i)
        # print(f"{joueur_enfile.get_nom()} a été ajouté à la file d'attente")
        ordre.enfiler(joueur_enfile)


# fait que l'utilisateur choisit une carte de sa famille dominante
# ptit pb : les deux joueurs demandent la mm carte pdt un long moment et jsp pk
def choisir_carte_demandee(joueur: Joueur):  # Johann
    # compte le nombre de cartes par familles à l'aide d'un dictionnaire avec
    # la clé : famille
    # valeur : nombre de carte de ctete famille dans la main du joueur
    comptfamille = {}
    for i in range(1, joueur.get_main().taille() + 1):
        carte = joueur.get_main().parcourir_jusqua(i)
        if carte is not None:
            famille_nom = carte.get_famille().get_nom()
            if not famille_nom in comptfamille:
                comptfamille[famille_nom] = 1
            else:
                comptfamille[famille_nom] += 1

    # Détermine la famille avec le plus grand nombre de membres dans la main du joueur
    famille_dominante = ""
    max_famille_dominante = -1
    for famille in fam:
        if famille in comptfamille:
            if comptfamille[famille] > max_famille_dominante:
                max_famille_dominante = comptfamille[famille]
                famille_dominante = famille
    # Détermine la carte précise de la famille à demander
    for i in range(1, joueur.get_main().taille() + 1):
        for membre in membres:
            if not chaines_pareilles(joueur.get_main().parcourir_jusqua(i).get_membre(), membre):
                carte_choisie = Carte(Famille(famille_dominante, 0), membre, True)
                return carte_choisie


# le joueur demande la carte à un autre
def demander_carte(joueur: Joueur, carte: Carte):  # Johann
    main_joueur = joueur.get_main()
    liste_joueurs_sans_demandeur = ListeJoueur()  # liste des joueurs sans celui qui demande, ainsi il choisira sa cible parmi les autres joueurs
    i = 1
    while i < liste_joueurs.taille() + 1:
        if not chaines_pareilles(liste_joueurs.parcourir_jusqua(i).get_nom(), joueur.get_nom()):
            joueur_add = liste_joueurs.parcourir_jusqua(i)
            liste_joueurs_sans_demandeur.ajouter_joueur(joueur_add)
            i += 1
        else:
            i += 1
    # joueur_cible=liste_joueurs_sans_demandeur.parcourir_jusqua(1)
    joueur_cible = liste_joueurs_sans_demandeur.parcourir_jusqua(randint(1, liste_joueurs_sans_demandeur.taille()))
    if not joueur_cible.get_main().__contains__(carte):
        if not pioche.est_vide():
            print(f"{joueur_cible.get_nom()} n'a pas la carte demandée, {joueur.get_nom()} pioche une carte")
            piocher(joueur)
        else:
            print("la pioche est vide")
    else:
        joueur_cible.get_main().suppr(carte)
        print(
            f"{joueur_cible.get_nom()} donne la carte {carte.get_membre()} de la famille {carte.get_famille().get_nom()} à {joueur.get_nom()}")
        main_joueur.ajouter_carte(carte)


# le joueur pioche un carte
def piocher(joueur: Joueur):  # Johann
    if not pioche.est_vide():
        carte_piochee = pioche.depiler()
        joueur.get_main().ajouter_carte(carte_piochee)


# vérifie si le joueur possede ou non une famille complète
def possede_famille(joueur: Joueur, famille: str):  # Johann
    nbmembres = 0
    for membre in membres:
        if joueur.get_main().contains_membre(famille, membre):
            nbmembres += 1
            print(famille, membre, "est possédé")
    if nbmembres == 6:
        return True
    return False


# le joueur constitue une famille
def constituer_famille(nomFamille, joueur: Joueur):  # Johann
    for membre in membres:
        print(f"suppression de la carte {membre} de la famille {nomFamille}")
        joueur.get_main().suppr(Carte(Famille(nomFamille, 0), membre, True))
    print(f"{joueur.get_nom()} vient de compléter la famille {nomFamille}")


start_game()