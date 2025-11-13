from graphics import *
from constantes import *

#i = colonne
#j = ligne
#f = fenetre

def dessiner_case(f,i,j):

    p1=(0+DIMENSION_CASE*i,0+DIMENSION_CASE*j)
    p2=(DIMENSION_CASE*(i+1),DIMENSION_CASE*(j+1))
    # creation d'un rectangle bleu
    draw_fill_rectangle(p1,p2,bleu,f)
    centre=(int(p2[0]-DIMENSION_CASE/2),int(p2[1]-DIMENSION_CASE/2))
    # creation d'un cercle blanc
    draw_fill_circle(centre,RAYON,blanc,f)

def dessiner_grille(couleur,f):

    # boucle sur le nombre de colonnes
    for i in range(0,NOMBRE_COLONNES):
        # boucle sur le nombre de cases
        for j in range(0,NOMBRE_LIGNES):
            dessiner_case(f,i,j)

def dessiner_pion(colonne,case,couleur,fenetre):

    # en fonctioin de si une case est prise ou non on calcule la cordonne du centre du pion a afficher
    abs_centre = int(DIMENSION_CASE/2 + (colonne - 1)*DIMENSION_CASE)
    ord_centre = int(DIMENSION_CASE/2 + (NOMBRE_LIGNES - case - 1)*DIMENSION_CASE)
    centre = (abs_centre,ord_centre)
    draw_fill_circle(centre,RAYON,couleur,fenetre)

def dessiner_zone_console(fenetre):
    """Dessine le fond noir de la zone console sur toute la largeur"""
    y_console = DIMENSION_CASE * NOMBRE_LIGNES
    largeur_fenetre = DIMENSION_CASE * NOMBRE_COLONNES
    
    # Fond noir pour TOUTE la zone des timers (toute la largeur)
    p1 = (0, y_console)
    p2 = (largeur_fenetre, y_console + DIMENSION_CONSOLE_LARGEUR)
    draw_fill_rectangle(p1, p2, noir, fenetre)

def ecrire_partie_terminee(f, pseudo_gagnant, couleur_gagnant):
    """Affiche un message de victoire au centre de l'écran dans un gros carré"""
    # Carré au centre
    largeur_carre = 400
    hauteur_carre = 150
    x = (DIMENSION_CASE * NOMBRE_COLONNES - largeur_carre) // 2
    y = (DIMENSION_CASE * NOMBRE_LIGNES - hauteur_carre) // 2
    
    # Fond blanc avec bordure noire
    p1 = (x, y)
    p2 = (x + largeur_carre, y + hauteur_carre)
    draw_fill_rectangle(p1, p2, blanc, f)
    draw_rectangle(p1, p2, noir, f)
    
    # Texte
    texte = f"{pseudo_gagnant} à gagné !"
    # Centrer le texte en fonction de sa longueur
    taille_texte = len(texte) * 15
    x_texte = x + (largeur_carre - taille_texte) // 2
    ecrire(texte, (x_texte, y + 40), 40, couleur_gagnant, f)

def ecrire_partie_nulle(f):
    """Affiche un message de partie nulle au centre de l'écran dans un gros carré"""
    # Carré au centre
    largeur_carre = 400
    hauteur_carre = 150
    x = (DIMENSION_CASE * NOMBRE_COLONNES - largeur_carre) // 2
    y = (DIMENSION_CASE * NOMBRE_LIGNES - hauteur_carre) // 2
    
    # Fond blanc avec bordure noire
    p1 = (x, y)
    p2 = (x + largeur_carre, y + hauteur_carre)
    draw_fill_rectangle(p1, p2, blanc, f)
    draw_rectangle(p1, p2, noir, f)
    
    # Texte
    ecrire("Partie nulle !", (x + 80, y + 50), 40, noir, f)