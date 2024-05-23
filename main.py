# Projet pendu Baptiste CORN

from random import choice


# On récupère le fichier pour les mots du pendu
def ouverture_fichier():
    # l'utilisateur choisit le fichier qu'il veut, personnalisé ou par défaut
    choix_du_fichier = int(input(
        "Voulez-vous une banque de mot personnalisé ou par défaut ? \n1 : Personnalisée\n2 : Par défaut\n"
        "Attention au chemin du fichier ! \n"))
    if choix_du_fichier == 1:
        fichier_utilisateur = input("veuillez saisir un nom de fichier texte, attention au chemin du fichier")
        fichier = open(fichier_utilisateur, "r", encoding="utf-8")
    elif choix_du_fichier == 2:
        fichier_utilisateur = input("choisissez le fichier texte par défaut mots_pendu.txt\n")
        fichier = open(fichier_utilisateur, "r", encoding="utf-8")
    else:
        print("ouverture par défaut")
        fichier = open("mots_pendu.txt", "r", encoding="utf-8")

    return fichier


def ecrire_fichier_dans_chaine(fichier):
    # On ecrit le fichier dans une liste pour pouvoir manipuler les mots dans le script
    banque_de_mots = fichier.read().splitlines()
    return banque_de_mots


def mot_aleatoire(banque_de_mots):
    # On choisit un mot aléatoire que le joueur va devoir deviner
    mot_a_deviner = choice(banque_de_mots)
    return mot_a_deviner


def supprimer_accent(mot_choisi):
    # Cette fonction sert à supprimer les accents du mot choisit aléatoirement
    # On declare une liste avec les accents présents dans la liste de mot
    liste_accent = ['à', 'é', 'è', 'ê', 'î', 'ô', 'ù', 'û']

    # On déclare une seconde liste sans accent pour les remplacer
    liste_sans_accent = ['a', 'e', 'e', 'e', 'i', 'o', 'u', 'u']

    # initialisation de la variable qui contiendra le mot sans les accents
    mot_sans_accent = ""

    for i in range(len(mot_choisi)):  # On parcourt le mot
        if mot_choisi[i] in liste_accent:  # Si une lettre du mot contient un accent present dans la liste_accent

            # On réécrit le mot sans les accents
            mot_sans_accent += liste_sans_accent[liste_accent.index(mot_choisi[i])]

        else:  # Sinon on recopie juste le mot
            mot_sans_accent += mot_choisi[i]

    return mot_sans_accent


def affichage_mot(mot_sans_accent):
    # cette fonction sert a afficher le mot sous forme de tiret "_" pour aider visuellement le joueur
    mot_cache = []
    for i in range(len(mot_sans_accent)):
        mot_cache = len(mot_sans_accent) * ['_']

    return mot_cache


# Debut de la boucle pour le jeu du pendu
def jeu_pendu(mon_mot, mot_cache):
    vie_du_joueur = 6  # Le joueur possède 6 vies au début de la partie
    compteur = 0  # Pour remplir la condition de victoire

    # Cette liste est utilisée pour donner un indice au joueur lorqu'il n'a plus qu'une vie
    liste_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print("Bienvenue au jeu du pendu, essayez de deviner le mot !")
    print(f'le mot contient {len(mon_mot)} lettres, bon courage ! ')

    # Boucle de jeu
    while vie_du_joueur != 0:
        print(f'Il vous reste {vie_du_joueur} vie(s)')
        print(mot_cache)  # On affiche le mot sous forme de tiret
        lettre = "null"

        while len(lettre) != 1:  # On s'assure que l'utilisateur ne peut choisir qu'une seule lettre à la fois
            lettre = input("\nveuillez choisir une lettre minuscule : ")

        if lettre in mon_mot:  # On affiche la lettre à la place du tiret si elle est présente dans le mot

            # La boucle sert à afficher plusieurs fois la même lettre si le mot possède des doubloons
            for i in range(len(mon_mot)):
                if lettre == mon_mot[i]:
                    del mot_cache[i]
                    mot_cache.insert(i, lettre)
                    compteur += 1
        else:
            print("ce n'est pas la bonne lettre, vous perdez une vie\n")
            vie_du_joueur -= 1

            # Indice pour le joueur s'il n'a plus qu'une vie
            if vie_du_joueur == 1:
                for i in range(len(mon_mot)):
                    if mon_mot[i] in liste_alphabet:
                        liste_alphabet.remove(mon_mot[i])  # On supprime les lettres du mot présentes dans l'alphabet

                indice = choice(liste_alphabet)
                # On affiche une lettre qui n'est pas dans le mot
                print(f'indice : la lettre suivante n est pas dans le mot : {indice}')

        # Condition de victoire
        if compteur == len(mot_cache):
            choix = 0
            print(f'Bravo, vous avez trouvé le mot {mon_mot}!')

            while choix != 1 or choix != 2:
                choix = int(
                    input("Voulez vous refaire une partie ? \n1 : Rejouer  \n2 : Arreter le programme\nchoix : "))
                if choix == 1:
                    recommencer()  # Fonction pour recommencer le jeu avec un nouveau mot
                elif choix == 2:
                    print("Au revoir")
                    return 0
        # Si le joueur a perdu toutes ses vies
        elif vie_du_joueur == 0:
            print(f'vous avez perdu\nLe mot était {mon_mot}')
            choix = 0
            while choix != 1 or choix != 2:
                choix = int(
                    input("Voulez vous refaire une partie ? \n1 : Rejouer  \n2 : Arreter le programme\nchoix : "))
                if choix == 1:
                    recommencer()  # Fonction pour recommencer le jeu avec un nouveau mot
                elif choix == 2:
                    print("Au revoir")
                    return 0


def initialisation():
    fichier = ouverture_fichier()
    liste_mots = ecrire_fichier_dans_chaine(fichier)
    mot_a_deviner = mot_aleatoire(liste_mots)
    mon_mot = supprimer_accent(mot_a_deviner)
    print(f'Pour aider a la correction, on donne le mot choisit aléatoirement : {mon_mot}')
    mot_cache = affichage_mot(mon_mot)
    jeu_pendu(mon_mot, mot_cache)


def recommencer():
    fichier = ouverture_fichier()
    liste_mots = ecrire_fichier_dans_chaine(fichier)
    mot_a_deviner = mot_aleatoire(liste_mots)
    mon_mot = supprimer_accent(mot_a_deviner)
    print(f'Pour aider a la correction, on donne le mot choisit aléatoirement : {mon_mot}\n')
    mot_cache = affichage_mot(mon_mot)
    jeu_pendu(mon_mot, mot_cache)


initialisation()
