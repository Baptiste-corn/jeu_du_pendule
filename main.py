# Projet pendu Baptiste CORN

from random import choice

# On récupère le fichier pour les mots du pendu
def ouverture_fichier () :
    choix_du_fichier = 0 # initialisation de la variable
    choix_du_fichier = int(input(
        "Voulez-vous une banque de mot personnalisé ou par défaut ? \n1 : Personnalisée\n2 : Par défaut\n"))
    if choix_du_fichier == 1:
        fichier_utilisateur = input("veuillez chosir un fichier (seconde_liste.txt)")
        fichier = open(fichier_utilisateur, "r", encoding="utf-8")
    elif choix_du_fichier == 2:
        fichier = open("mots_pendu.txt", "r",encoding="utf-8")
        # with open("C:/Users/bapti/Desktop/ETS/Ete_2024/MGA802/projetPendu/mots_pendu.txt", "r") as fio:
        #   fichier = fio.read().splitlines()
    else:
        print("ouverture par défaut")
        with open("C:/Users/bapti/Desktop/ETS/Ete_2024/MGA802/projetPendu/mots_pendu.txt", "r") as fio:
            fichier = fio.read().splitlines()

    return fichier


def ecrire_fichier_dans_chaine(fichier):
    banque_de_mots = fichier.read().splitlines()
    return banque_de_mots

def mot_aleatoire(banque_de_mots):
    mot_a_deviner = choice(banque_de_mots)
    return mot_a_deviner

def supprimer_accent (mot_choisi):
    liste_accent = ['à', 'é', 'è', 'ê', 'î', 'ô', 'ù', 'û']
    liste_sans_accent = ['a', 'e', 'e', 'e', 'i', 'o', 'u', 'u']
    mot_sans_accent = ""

    for i in range(len(mot_choisi)): # On parcourt le mot
        if mot_choisi[i] in liste_accent : # Si une lettre du mot contient un accent present dans la liste_accent
            mot_sans_accent += liste_sans_accent[liste_accent.index(mot_choisi[i])]
            # On concatene notre liste avec la lettre sans accent
        else:
            mot_sans_accent += mot_choisi[i]

    return mot_sans_accent

def affichage_mot (mot_sans_accent):

    for i in range(len(mot_sans_accent)):
        mot_cache = len(mot_sans_accent) * ['_']

    return mot_cache

# Le mot est choisi aléatoirement et les accents sont retires


# Debut de la boucle pour le jeu du pendu


def jeu_pendu(mon_mot, mot_cache):

    vie_du_joueur = 6
    compteur = 0  # Pour remplir la condition de victoire
    print("Bienvenue au jeu du pendu, essayez de deviner le mot !")
    print(f'le mot contient {len(mon_mot)} lettres, bon courage ! ')

    while vie_du_joueur != 0:
        print(f'Il vous reste {vie_du_joueur}')
        print(mot_cache)
        lettre = "null"


        while len(lettre) != 1:
            lettre = input("veuillez choisir une lettre minuscule : ")

        if lettre in mon_mot:
            del mot_cache[mon_mot.index(lettre)]
            mot_cache.insert(mon_mot.index(lettre), lettre)
            compteur += 1


        else:
            print("ce n'est pas la bonne lettre, vous perdez une vie")
            vie_du_joueur -= 1


        # Condition de victoire
        if compteur == len(mot_cache):
            choix = 0
            print ("Bravo, vous avez trouvé le mot !")
            print(mon_mot)
            while choix != 1 or choix != 2:
                choix = int(input("Voulez vous refaire une partie ? \n1 : Rejouer  \n2 : Arreter le programme\nchoix : "))
                if choix == 1:
                    recommencer()
                elif choix == 2:
                    print("Au revoir")
                    return 0





def initialisation():
    fichier = ouverture_fichier()
    liste_mots = ecrire_fichier_dans_chaine(fichier)
    mot_a_deviner = mot_aleatoire(liste_mots)
    mon_mot = supprimer_accent(mot_a_deviner)
    print(mon_mot)
    mot_cache = affichage_mot(mon_mot)
    jeu_pendu(mon_mot, mot_cache)


def recommencer ():

    fichier = ouverture_fichier()
    liste_mots = ecrire_fichier_dans_chaine(fichier)
    mot_a_deviner = mot_aleatoire(liste_mots)
    mon_mot = supprimer_accent(mot_a_deviner)
    print(mon_mot)
    mot_cache = affichage_mot(mon_mot)
    jeu_pendu(mon_mot, mot_cache)


initialisation()
