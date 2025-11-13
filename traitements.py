from constantes import *
from graphiques import *

def selectionner_colonne(abscisse,grille):
    # déterminer la colonne
    indice_colonne = abscisse // DIMENSION_CASE + 1
    # rend la liste de la grille correspondant à la colonne
    colonne = grille[indice_colonne-1]
    # console
    print(f"la colonne {indice_colonne} contient {colonne}")
    # déterminer la prochaine case encore disponible
    if 0 in colonne:
        # prend l'indice de la colonne dans le tableau
        prochaine_case = colonne.index(0)
    else:
        # cela indique que la colonne est pleine
        prochaine_case = -1
    # console
    print(f"la prochaine case disponoible est {prochaine_case}")
    # retourne colonne et prochaine_case
    return indice_colonne,prochaine_case

def afficher_pion(colonne,case,joueur,couleur,grille,fenetre):
    # la case varie en fonction du nombre de nombre de pion dans la colonne
    if case >= 0:
        # afficher un pion
        dessiner_pion(colonne,case,couleur,fenetre)
        # afficher dans la grille qu'il y a deja un pion dans une case
        grille[colonne-1][case] = joueur

def alterner_joueur(joueur,couleur,prochaine_case):
    # lorsqu'une colonne est pleine il n'alterne pas le joueur
    if prochaine_case == -1:
        return joueur, couleur

    if joueur == 1:
        # on met joueur = 2
        joueur = 2
        # on met couleur = rouge
        couleur = rouge
    else:
        # on met joueur = 1
        joueur = 1
        # on met couleur = jaune
        couleur = jaune

    return joueur, couleur

def verifier_gagnant(grille,joueur):
    sequence_gagnante = [joueur,joueur,joueur,joueur]

    # vertical
    # on se positionne sur une colonne
    for i in range(0,NOMBRE_COLONNES):
        colonne = grille[i]
        # on se positionne sur une ligne
        for j in range(0,NOMBRE_LIGNES-4):
            #selectionne les quatre pions
            if colonne[j:j+4] == sequence_gagnante:
                #console
                print("partie gagnée")
                return True

    # horizontal
    # on se positionne sur une ligne
    for i in range(0,NOMBRE_LIGNES):
        # on se positionne sur une colonne
        for j in range(0,NOMBRE_COLONNES-4):
            ligne = []
            # premiere case
            ligne.append(grille[j][i])
            # deuxieme case
            ligne.append(grille[j+1][i])
            # troisieme case
            ligne.append(grille[j+2][i])
            # quatrieme case
            ligne.append(grille[j+3][i])
            print(f"la prochaine ligne est {ligne}")
            if ligne == sequence_gagnante:
                    #console
                    print("partie gagnée")
                    return True

    # diagonale
    # on prend tous les tuples et on les met dans diagonales
    for diagonale in DIAGONALES:
        diag = []
        for i,j in diagonale:
            diag.append(grille[i][j])
        #console
        print(f"la diagonale est {diag}")

        # dans une diagonale il peut y avoir 3 puissance 4 par rapport a la longueur de la diagonale
        nombre_comparaisons = len(diagonale) - 3

        # on prend les quatre suivants
        for k in range(0,nombre_comparaisons):
            #console
            print(f"comparaison de {diag[k:4+k]} et {sequence_gagnante}")
            if diag[k:4+k] == sequence_gagnante:
                #console
                print("partie gagnée")
                return True

    return False

def verifier_nul(grille,gagnant,fenetre):
    # on cherche si il reste un 0 dans la grille
    for colonne in grille:
        if 0 in colonne:
            return False

    ecrire_partie_nulle(fenetre)
    attendre(4000)
    return True

def verifier_partie(nul,gagnant,fenetre,joueur,couleur_joueur):
    if gagnant == True:
        ecrire_partie_terminee(fenetre, joueur, couleur_joueur)
        attendre(2000)
        return True

    if nul == True:
        ecrire_partie_nulle(fenetre)
        attendre(2000)
        return True

    return False