from graphics import *
from graphiques import *
from traitements import *
from timer import *
from menu import *

print("="*50)
print("DEMARRAGE DU JEU PUISSANCE 4")
print("="*50)

# Init fenêtre
fenetre = init_graphics(DIMENSION_CASE*NOMBRE_COLONNES, DIMENSION_CASE*NOMBRE_LIGNES+DIMENSION_CONSOLE_LARGEUR)
print(f"[INIT] Fenêtre créée: {DIMENSION_CASE*NOMBRE_COLONNES}x{DIMENSION_CASE*NOMBRE_LIGNES+DIMENSION_CONSOLE_LARGEUR}")

# Compteur de victoires
victoires_j1 = 0
victoires_j2 = 0
parties_nulles = 0
pseudo_j1 = "Joueur 1"
pseudo_j2 = "Joueur 2"
print(f"[INIT] Compteur de victoires initialisé: J1={victoires_j1}, J2={victoires_j2}, Nuls={parties_nulles}")

# Boucle principale du jeu
continuer_jeu = True
couleur_j1 = None
couleur_j2 = None

while continuer_jeu:
    print("\n" + "="*50)
    print("NOUVELLE ITERATION - Menu principal")
    print("="*50)
    
    # Afficher le menu principal
    continuer_jeu = menu_principal(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
    
    if not continuer_jeu:
        print(f"[JEU] Fin du jeu demandée")
        break
    
    # Sélection des couleurs et pseudos (uniquement si pas encore définis)
    if couleur_j1 is None or couleur_j2 is None:
        print(f"[JEU] Lancement de la sélection des pseudos et couleurs")
        couleur_j1, couleur_j2, pseudo_j1, pseudo_j2 = menu_selection_couleurs(fenetre)
    else:
        print(f"[JEU] Utilisation des couleurs et pseudos existants: {pseudo_j1} vs {pseudo_j2}")
    
    # Initialiser la grille
    grille = [[0,0,0,0,0,0], \
        [0,0,0,0,0,0], \
        [0,0,0,0,0,0], \
        [0,0,0,0,0,0], \
        [0,0,0,0,0,0], \
        [0,0,0,0,0,0], \
        [0,0,0,0,0,0]]
    print(f"[JEU] Grille initialisée")
    
    # Variables de jeu
    joueur = 1
    couleur_pion = couleur_j1
    print(f"[JEU] Joueur initial: {joueur}, Couleur: {couleur_pion}")
    
    # Initialiser les timers
    initialiser_timers()
    print(f"[JEU] Timers initialisés")
    
    # Dessiner la grille
    dessiner_grille(bleu, fenetre)
    print(f"[JEU] Grille dessinée")
    
    # Afficher timer et score initial
    afficher_timers(fenetre, joueur, couleur_j1, couleur_j2, pseudo_j1, pseudo_j2)
    afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
    
    # Boucle de jeu
    partie_terminee = False
    gagnant_timeout = 0  # 0 = pas de timeout, 1 = J1 gagne, 2 = J2 gagne
    retour_menu = False  # Pour savoir si on retourne au menu depuis la pause
    
    print(f"[JEU] Début de la partie")
    print("="*50)
    
    while partie_terminee == False and not retour_menu:
        # Mettre à jour le timer
        gagnant_timeout = mettre_a_jour_timer(joueur)
        
        if gagnant_timeout > 0:
            if gagnant_timeout == 2:
                print(f"[TIMER] Temps écoulé pour Joueur 1! Joueur 2 gagne par timeout")
            else:
                print(f"[TIMER] Temps écoulé pour Joueur 2! Joueur 1 gagne par timeout")
            partie_terminee = True
        
        # Afficher le timer mis à jour
        afficher_timers(fenetre, joueur, couleur_j1, couleur_j2, pseudo_j1, pseudo_j2)
        afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
        
        # Attendre un événement avec timeout
        evenement = None
        for evt in pygame.event.get():
            if evt.type == pygame.MOUSEBUTTONUP or evt.type == pygame.QUIT:
                evenement = evt
                break
            elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
                # Menu pause
                print(f"[EVENT] ESC pressé - Menu pause")
                mettre_en_pause_timer()
                
                # Redessiner la grille avec tous les pions
                dessiner_grille(bleu, fenetre)
                for i in range(NOMBRE_COLONNES):
                    for j in range(NOMBRE_LIGNES):
                        if grille[i][j] == 1:
                            dessiner_pion(i+1, j, couleur_j1, fenetre)
                        elif grille[i][j] == 2:
                            dessiner_pion(i+1, j, couleur_j2, fenetre)
                
                continuer_partie = menu_pause(fenetre)
                
                if continuer_partie:
                    # Reprendre la partie
                    print(f"[EVENT] Reprise de la partie")
                    reprendre_timer()
                    # Redessiner la grille
                    dessiner_grille(bleu, fenetre)
                    for i in range(NOMBRE_COLONNES):
                        for j in range(NOMBRE_LIGNES):
                            if grille[i][j] == 1:
                                dessiner_pion(i+1, j, couleur_j1, fenetre)
                            elif grille[i][j] == 2:
                                dessiner_pion(i+1, j, couleur_j2, fenetre)
                    afficher_timers(fenetre, joueur, couleur_j1, couleur_j2, pseudo_j1, pseudo_j2)
                    afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
                else:
                    # Retour au menu - réinitialiser les compteurs
                    print(f"[EVENT] Retour au menu principal - RAZ des compteurs")
                    victoires_j1 = 0
                    victoires_j2 = 0
                    parties_nulles = 0
                    retour_menu = True
                    partie_terminee = True
                break
        
        if evenement is None:
            pygame.time.wait(50)  # Pause courte pour ne pas surcharger le CPU
            continue
        
        if evenement.type == pygame.MOUSEBUTTONUP:
            print(f"[EVENT] Clic souris détecté: position={evenement.pos}")
            
            # Vérifier si le clic est dans la zone de jeu
            if evenement.pos[1] >= DIMENSION_CASE * NOMBRE_LIGNES:
                print(f"[EVENT] Clic dans la zone console, ignoré")
                continue
            
            # Sélectionner une colonne
            colonne, prochaine_case = selectionner_colonne(evenement.pos[0], grille)
            print(f"[JEU] Colonne sélectionnée: {colonne}, Prochaine case: {prochaine_case}")
            
            # Afficher pion
            afficher_pion(colonne, prochaine_case, joueur, couleur_pion, grille, fenetre)
            print(f"[JEU] Pion affiché pour joueur {joueur}")
            
            # Vérifier si jeu gagnant
            gagnant = verifier_gagnant(grille, joueur)
            print(f"[JEU] Vérification gagnant: {gagnant}")
            
            # Vérifier si jeu nul
            partie_nulle = verifier_nul(grille, gagnant, fenetre)
            print(f"[JEU] Vérification partie nulle: {partie_nulle}")
            
            # Vérifier si la partie est terminée
            pseudo_actuel = pseudo_j1 if joueur == 1 else pseudo_j2
            partie_terminee = verifier_partie(partie_nulle, gagnant, fenetre, pseudo_actuel, couleur_pion)
            print(f"[JEU] Partie terminée: {partie_terminee}")
            
            if gagnant:
                if joueur == 1:
                    victoires_j1 += 1
                    print(f"[SCORE] Victoire {pseudo_j1}! Score: {pseudo_j1}={victoires_j1}, {pseudo_j2}={victoires_j2}")
                else:
                    victoires_j2 += 1
                    print(f"[SCORE] Victoire {pseudo_j2}! Score: {pseudo_j1}={victoires_j1}, {pseudo_j2}={victoires_j2}")
                
                # Mettre à jour le score affiché
                afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
            
            if partie_nulle:
                parties_nulles += 1
                print(f"[SCORE] Partie nulle! Nuls={parties_nulles}")
                afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
            
            # Alterner les joueurs
            ancien_joueur = joueur
            joueur, couleur_pion = alterner_joueur(joueur, couleur_pion, prochaine_case)
            print(f"[JEU] Alternance joueur: ancien={ancien_joueur}, nouveau={joueur}")
            
            # Si la couleur a changé, mettre à jour l'affichage
            if joueur == 1:
                couleur_pion = couleur_j1
            elif joueur == 2:
                couleur_pion = couleur_j2
        
        if evenement.type == pygame.QUIT:
            print(f"[EVENT] Fermeture fenêtre demandée")
            partie_terminee = True
            continuer_jeu = False
    
    # Ne gérer le timeout que si on n'est pas revenu au menu via pause
    if not retour_menu:
        # Gestion du timeout
        if gagnant_timeout > 0:
            if gagnant_timeout == 1:
                victoires_j1 += 1
                print(f"[SCORE] Victoire {pseudo_j1} par timeout! Score: {pseudo_j1}={victoires_j1}, {pseudo_j2}={victoires_j2}")
                ecrire(f"{pseudo_j1} gagne par timeout!", (150, DIMENSION_CASE*NOMBRE_LIGNES + 70), 22, jaune, fenetre)
            else:
                victoires_j2 += 1
                print(f"[SCORE] Victoire {pseudo_j2} par timeout! Score: {pseudo_j1}={victoires_j1}, {pseudo_j2}={victoires_j2}")
                ecrire(f"{pseudo_j2} gagne par timeout!", (150, DIMENSION_CASE*NOMBRE_LIGNES + 70), 22, rouge, fenetre)
            
            afficher_timers(fenetre, joueur, couleur_j1, couleur_j2, pseudo_j1, pseudo_j2)
            afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1, pseudo_j2)
            attendre(3000)
        
        # Menu de fin de partie (sauf si on a quitté)
        if partie_terminee and continuer_jeu:
            choix = menu_fin_partie(fenetre)
            
            if choix == 'continuer':
                print(f"[MENU] Continuer - Nouvelle partie avec mêmes couleurs et pseudos")
                # La boucle va recommencer avec les mêmes couleurs et pseudos
            elif choix == 'modifier':
                print(f"[MENU] Modifier les couleurs et pseudos")
                couleur_j1, couleur_j2, pseudo_j1, pseudo_j2 = menu_selection_couleurs(fenetre, pseudo_j1, pseudo_j2)
            elif choix == 'nouveau':
                print(f"[MENU] Nouvelle partie - RAZ des compteurs et retour au menu")
                victoires_j1 = 0
                victoires_j2 = 0
                parties_nulles = 0
                couleur_j1 = None
                couleur_j2 = None
                # Ne pas réinitialiser les pseudos, ils seront redemandés
            elif choix == 'quitter':
                print(f"[MENU] Quitter le jeu")
                continuer_jeu = False
    
    print(f"[JEU] Fin de la partie")

# Fin du programme
print("="*50)
print("FIN DU JEU PUISSANCE 4")
print(f"Score final: {pseudo_j1}: {victoires_j1} - {pseudo_j2}: {victoires_j2} - Nuls: {parties_nulles}")
print("="*50)
quit_graphics()