from graphics import *
from constantes import *

def dessiner_bouton(fenetre, x, y, largeur, hauteur, texte, couleur, couleur_texte=noir):
    """Dessine un bouton rectangulaire"""
    p1 = (x, y)
    p2 = (x + largeur, y + hauteur)
    draw_fill_rectangle(p1, p2, couleur, fenetre)
    draw_rectangle(p1, p2, noir, fenetre)
    
    # Centrer le texte
    texte_x = x + largeur // 4
    texte_y = y + hauteur // 3
    ecrire(texte, (texte_x, texte_y), 20, couleur_texte, fenetre)

def clic_dans_zone(pos, x, y, largeur, hauteur):
    """Vérifie si un clic est dans une zone donnée"""
    return x <= pos[0] <= x + largeur and y <= pos[1] <= y + hauteur

def menu_pause(fenetre):
    """Menu de pause - Retourne True pour continuer, False pour retour au menu"""
    print(f"[MENU] Ouverture du menu de pause")
    
    # Semi-transparence: dessiner un rectangle gris semi-transparent
    largeur_fenetre = DIMENSION_CASE * NOMBRE_COLONNES
    hauteur_fenetre = DIMENSION_CASE * NOMBRE_LIGNES + DIMENSION_CONSOLE_LARGEUR
    
    # Créer une surface semi-transparente
    overlay = pygame.Surface((largeur_fenetre, hauteur_fenetre))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    fenetre.blit(overlay, (0, 0))
    
    # Titre
    ecrire("PAUSE", (250, 150), 50, blanc, fenetre)
    
    # Boutons
    dessiner_bouton(fenetre, 200, 250, 300, 60, "Continuer", vert, noir)
    dessiner_bouton(fenetre, 200, 340, 300, 60, "Retour au menu", rouge, blanc)
    
    affiche_all()
    
    # Attendre choix
    while True:
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONUP:
            # Continuer
            if clic_dans_zone(ev.pos, 200, 250, 300, 60):
                print(f"[MENU] Continuer sélectionné")
                return True
            # Retour au menu
            elif clic_dans_zone(ev.pos, 200, 340, 300, 60):
                print(f"[MENU] Retour au menu sélectionné")
                return False
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            # ESC pour continuer
            print(f"[MENU] ESC pour continuer")
            return True
        elif ev.type == pygame.QUIT:
            print(f"[MENU] Fermeture de la fenêtre")
            return False

def menu_fin_partie(fenetre):
    """Menu de fin de partie - Retourne 'continuer', 'modifier', 'acceuil', ou 'quitter'"""
    print(f"[MENU] Ouverture du menu de fin de partie")
    
    # Semi-transparence
    largeur_fenetre = DIMENSION_CASE * NOMBRE_COLONNES
    hauteur_fenetre = DIMENSION_CASE * NOMBRE_LIGNES + DIMENSION_CONSOLE_LARGEUR
    
    overlay = pygame.Surface((largeur_fenetre, hauteur_fenetre))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 0))
    fenetre.blit(overlay, (0, 0))
    
    # Boutons
    dessiner_bouton(fenetre, 150, 200, 200, 50, "Continuer", vert, noir)
    dessiner_bouton(fenetre, 400, 200, 200, 50, "Modifier", orange, noir)
    dessiner_bouton(fenetre, 150, 290, 200, 50, "Accueil", bleu, blanc)
    dessiner_bouton(fenetre, 400, 290, 200, 50, "Quitter", rouge, blanc)
    
    affiche_all()
    
    # Attendre choix
    while True:
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONUP:
            if clic_dans_zone(ev.pos, 150, 200, 200, 50):
                print(f"[MENU] Continuer sélectionné")
                return 'continuer'
            elif clic_dans_zone(ev.pos, 400, 200, 200, 50):
                print(f"[MENU] Modifier sélectionné")
                return 'modifier'
            elif clic_dans_zone(ev.pos, 150, 290, 200, 50):
                print(f"[MENU] Accueil sélectionnée")
                return 'acceuil'
            elif clic_dans_zone(ev.pos, 400, 290, 200, 50):
                print(f"[MENU] Quitter sélectionné")
                return 'quitter'
        elif ev.type == pygame.QUIT:
            print(f"[MENU] Fermeture de la fenêtre")
            return 'quitter'

def menu_selection_couleurs(fenetre, pseudo_j1=None, pseudo_j2=None):
    """Menu pour sélectionner les pseudos et couleurs des joueurs"""
    print(f"[MENU] Ouverture du menu de sélection des pseudos et couleurs")
    
    # Nettoyer l'écran
    fill_screen(blanc, fenetre)
    
    # Titre
    ecrire("PUISSANCE 4 - Selection", (150, 30), 30, noir, fenetre)
    
    # Saisie pseudo Joueur 1 si non fourni
    if pseudo_j1 is None:
        ecrire("Joueur 1 - Entrez votre pseudo:", (50, 80), 22, noir, fenetre)
        ecrire("(Appuyez sur ENTREE pour valider)", (50, 110), 16, gris, fenetre)
        affiche_all()
        
        pseudo_j1 = ""
        saisie_terminee = False
        message_erreur = ""
        
        while not saisie_terminee:
            ev = pygame.event.wait()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN and len(pseudo_j1) > 0:
                    # Vérifier si le pseudo est valide
                    if pseudo_est_valide(pseudo_j1):
                        saisie_terminee = True
                        message_erreur = ""
                    else:
                        message_erreur = "Pseudo interdit ! Choisissez-en un autre."
                        print(f"[MENU] Pseudo interdit: {pseudo_j1}")
                elif ev.key == pygame.K_BACKSPACE:
                    pseudo_j1 = pseudo_j1[:-1]
                    message_erreur = ""
                elif ev.unicode.isprintable() and len(pseudo_j1) < 15:
                    pseudo_j1 += ev.unicode
                
                # Réafficher
                fill_screen(blanc, fenetre)
                ecrire("PUISSANCE 4 - Selection", (150, 30), 30, noir, fenetre)
                ecrire("Joueur 1 - Entrez votre pseudo:", (50, 80), 22, noir, fenetre)
                ecrire("(Appuyez sur ENTREE pour valider)", (50, 110), 16, gris, fenetre)
                ecrire(pseudo_j1 + "_", (50, 150), 24, noir, fenetre)
                
                # Afficher message d'erreur si présent
                if message_erreur:
                    ecrire(message_erreur, (50, 190), 18, rouge, fenetre)
                
                affiche_all()
        
        print(f"[MENU] Pseudo Joueur 1: {pseudo_j1}")
    
    # Saisie pseudo Joueur 2 si non fourni
    if pseudo_j2 is None:
        fill_screen(blanc, fenetre)
        ecrire("PUISSANCE 4 - Selection", (150, 30), 30, noir, fenetre)
        ecrire(f"Joueur 1: {pseudo_j1}", (50, 70), 20, noir, fenetre)
        ecrire("Joueur 2 - Entrez votre pseudo:", (50, 110), 22, noir, fenetre)
        ecrire("(Appuyez sur ENTREE pour valider)", (50, 140), 16, gris, fenetre)
        affiche_all()
        
        pseudo_j2 = ""
        saisie_terminee = False
        message_erreur = ""
        
        while not saisie_terminee:
            ev = pygame.event.wait()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN and len(pseudo_j2) > 0:
                    # Vérifier si le pseudo est valide
                    if pseudo_est_valide(pseudo_j2):
                        saisie_terminee = True
                        message_erreur = ""
                    else:
                        message_erreur = "Pseudo interdit ! Choisissez-en un autre."
                        print(f"[MENU] Pseudo interdit: {pseudo_j2}")
                elif ev.key == pygame.K_BACKSPACE:
                    pseudo_j2 = pseudo_j2[:-1]
                    message_erreur = ""
                elif ev.unicode.isprintable() and len(pseudo_j2) < 15:
                    pseudo_j2 += ev.unicode
                
                # Réafficher
                fill_screen(blanc, fenetre)
                ecrire("PUISSANCE 4 - Selection", (150, 30), 30, noir, fenetre)
                ecrire(f"Joueur 1: {pseudo_j1}", (50, 70), 20, noir, fenetre)
                ecrire("Joueur 2 - Entrez votre pseudo:", (50, 110), 22, noir, fenetre)
                ecrire("(Appuyez sur ENTREE pour valider)", (50, 140), 16, gris, fenetre)
                ecrire(pseudo_j2 + "_", (50, 180), 24, noir, fenetre)
                
                # Afficher message d'erreur si présent
                if message_erreur:
                    ecrire(message_erreur, (50, 220), 18, rouge, fenetre)
                
                affiche_all()
        
        print(f"[MENU] Pseudo Joueur 2: {pseudo_j2}")
    
    # Nettoyer l'écran pour les couleurs
    fill_screen(blanc, fenetre)
    
    # Titre
    ecrire("PUISSANCE 4 - Selection des couleurs", (50, 30), 30, noir, fenetre)
    ecrire(f"{pseudo_j1} - Choisissez votre couleur:", (50, 100), 22, noir, fenetre)
    
    # Couleurs disponibles
    couleurs_dispo = [
        ("Jaune", jaune, noir),
        ("Rouge", rouge, blanc),
        ("Vert", vert, noir),
        ("Bleu Marine", bleumarine, blanc),
        ("Orange", orange, noir),
        ("Violet", violet, blanc),
        ("Cyan", cyan, noir),
        ("Magenta", magenta, blanc)
    ]
    
    # Dessiner les boutons de couleur pour Joueur 1
    y_start = 150
    boutons_j1 = []
    for i, (nom, couleur, texte_couleur) in enumerate(couleurs_dispo):
        x = 50 + (i % 4) * 160
        y = y_start + (i // 4) * 80
        dessiner_bouton(fenetre, x, y, 140, 60, nom, couleur, texte_couleur)
        boutons_j1.append((x, y, 140, 60, couleur, nom))
    
    affiche_all()
    
    # Attendre sélection Joueur 1
    couleur_j1 = None
    nom_j1 = None
    while couleur_j1 is None:
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONUP:
            for x, y, w, h, couleur, nom in boutons_j1:
                if clic_dans_zone(ev.pos, x, y, w, h):
                    couleur_j1 = couleur
                    nom_j1 = nom
                    print(f"[MENU] {pseudo_j1} a choisi: {nom_j1}")
                    break
    
    # Nettoyer et afficher choix Joueur 2
    fill_screen(blanc, fenetre)
    ecrire("PUISSANCE 4 - Selection des couleurs", (50, 30), 30, noir, fenetre)
    ecrire(f"{pseudo_j1}: {nom_j1}", (50, 80), 22, couleur_j1, fenetre)
    ecrire(f"{pseudo_j2} - Choisissez votre couleur:", (50, 120), 22, noir, fenetre)
    
    # Dessiner les boutons pour Joueur 2 (sans la couleur du Joueur 1)
    y_start = 170
    boutons_j2 = []
    for i, (nom, couleur, texte_couleur) in enumerate(couleurs_dispo):
        if couleur != couleur_j1:  # Interdire la même couleur
            x = 50 + (len(boutons_j2) % 4) * 160
            y = y_start + (len(boutons_j2) // 4) * 80
            dessiner_bouton(fenetre, x, y, 140, 60, nom, couleur, texte_couleur)
            boutons_j2.append((x, y, 140, 60, couleur, nom))
    
    affiche_all()
    
    # Attendre sélection Joueur 2
    couleur_j2 = None
    nom_j2 = None
    while couleur_j2 is None:
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONUP:
            for x, y, w, h, couleur, nom in boutons_j2:
                if clic_dans_zone(ev.pos, x, y, w, h):
                    couleur_j2 = couleur
                    nom_j2 = nom
                    print(f"[MENU] {pseudo_j2} a choisi: {nom_j2}")
                    break
    
    print(f"[MENU] Couleurs sélectionnées - {pseudo_j1}: {nom_j1}, {pseudo_j2}: {nom_j2}")
    return couleur_j1, couleur_j2, pseudo_j1, pseudo_j2

def menu_principal(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1="Joueur 1", pseudo_j2="Joueur 2"):
    """Menu principal avec option nouvelle partie ou quitter"""
    print(f"[MENU] Affichage du menu principal")
    
    fill_screen(bleu, fenetre)
    
    # Titre
    ecrire("PUISSANCE 4", (200, 100), 50, jaune, fenetre)
    
    # Afficher le score
    if victoires_j1 > 0 or victoires_j2 > 0 or parties_nulles > 0:
        score_text = f"{pseudo_j1}: {victoires_j1} - {pseudo_j2}: {victoires_j2} - Nuls: {parties_nulles}"
        ecrire(score_text, (80, 200), 22, blanc, fenetre)
    
    # Boutons
    dessiner_bouton(fenetre, 200, 280, 300, 60, "Nouvelle Partie", vert, noir)
    dessiner_bouton(fenetre, 200, 370, 300, 60, "Quitter", rouge, blanc)
    
    affiche_all()
    
    # Attendre choix
    while True:
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONUP:
            # Nouvelle partie
            if clic_dans_zone(ev.pos, 200, 280, 300, 60):
                print(f"[MENU] Nouvelle partie sélectionnée")
                return True
            # Quitter
            elif clic_dans_zone(ev.pos, 200, 370, 300, 60):
                print(f"[MENU] Quitter sélectionné")
                return False
        elif ev.type == pygame.QUIT:
            print(f"[MENU] Fermeture de la fenêtre")
            return False