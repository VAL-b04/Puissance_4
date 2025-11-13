import time
from graphics import *
from constantes import *

# Variables globales pour les timers
temps_j1 = 0
temps_j2 = 0
dernier_temps = 0
TEMPS_LIMITE = 300  # 5 minutes par joueur
timer_en_pause = False
timer_en_pause = False

def initialiser_timers():
    """Initialise les timers pour une nouvelle partie"""
    global temps_j1, temps_j2, dernier_temps, timer_en_pause
    temps_j1 = TEMPS_LIMITE
    temps_j2 = TEMPS_LIMITE
    dernier_temps = time.time()
    timer_en_pause = False
    print(f"[TIMER] Timers initialisés: J1={temps_j1}s, J2={temps_j2}s")

def mettre_en_pause_timer():
    """Met le timer en pause"""
    global timer_en_pause
    timer_en_pause = True
    print(f"[TIMER] Timer mis en pause")

def reprendre_timer():
    """Reprend le timer"""
    global timer_en_pause, dernier_temps
    timer_en_pause = False
    dernier_temps = time.time()  # Réinitialiser le temps de référence
    print(f"[TIMER] Timer repris")

def mettre_a_jour_timer(joueur_actuel):
    """
    Met à jour le timer du joueur actuel
    Retourne:
        0 si tout va bien
        1 si Joueur 1 gagne par timeout (J2 a dépassé le temps)
        2 si Joueur 2 gagne par timeout (J1 a dépassé le temps)
    """
    global temps_j1, temps_j2, dernier_temps
    
    # Ne pas mettre à jour si en pause
    if timer_en_pause:
        return 0
    
    temps_actuel = time.time()
    temps_ecoule = temps_actuel - dernier_temps
    dernier_temps = temps_actuel
    
    if joueur_actuel == 1:
        temps_j1 -= temps_ecoule
        if temps_j1 <= 0:
            temps_j1 = 0
            print(f"[TIMER] Joueur 1 à court de temps!")
            return 2  # Joueur 2 gagne
    else:
        temps_j2 -= temps_ecoule
        if temps_j2 <= 0:
            temps_j2 = 0
            print(f"[TIMER] Joueur 2 à court de temps!")
            return 1  # Joueur 1 gagne
    
    return 0  # Pas de timeout

def afficher_timers(fenetre, joueur_actuel, couleur_j1, couleur_j2, pseudo_j1="Joueur 1", pseudo_j2="Joueur 2"):
    """Affiche les timers dans la zone console"""
    from graphiques import dessiner_zone_console
    
    y_console = DIMENSION_CASE * NOMBRE_LIGNES
    
    # Dessiner le fond noir (délégué à graphiques.py)
    dessiner_zone_console(fenetre)
    
    # Calculer minutes et secondes
    minutes_j1 = int(temps_j1 // 60)
    secondes_j1 = int(temps_j1 % 60)
    minutes_j2 = int(temps_j2 // 60)
    secondes_j2 = int(temps_j2 % 60)
    
    # Timer Joueur 1
    timer_text_j1 = f"{pseudo_j1}: {minutes_j1:02d}:{secondes_j1:02d}"
    couleur_timer_j1 = couleur_j1 if joueur_actuel == 1 else gris
    ecrire(timer_text_j1, (20, y_console + 10), 20, couleur_timer_j1, fenetre)
    
    # Timer Joueur 2
    timer_text_j2 = f"{pseudo_j2}: {minutes_j2:02d}:{secondes_j2:02d}"
    couleur_timer_j2 = couleur_j2 if joueur_actuel == 2 else gris
    ecrire(timer_text_j2, (20, y_console + 45), 20, couleur_timer_j2, fenetre)
    
    # Afficher au tour de qui c'est
    couleur_actuelle = couleur_j1 if joueur_actuel == 1 else couleur_j2
    pseudo_actuel = pseudo_j1 if joueur_actuel == 1 else pseudo_j2
    tour_text = f"Au tour de: {pseudo_actuel}"
    ecrire(tour_text, (250, y_console + 10), 22, couleur_actuelle, fenetre)

def afficher_score(fenetre, victoires_j1, victoires_j2, parties_nulles, pseudo_j1="Joueur 1", pseudo_j2="Joueur 2"):
    """Affiche le compteur de victoires et nulles dans la zone console"""
    y_console = DIMENSION_CASE * NOMBRE_LIGNES
    
    # Afficher le compteur de victoires (version abrégée pour l'espace)
    score_text = f"{pseudo_j1[:8]}: {victoires_j1} | {pseudo_j2[:8]}: {victoires_j2} | Nuls: {parties_nulles}"
    ecrire(score_text, (250, y_console + 45), 18, blanc, fenetre)

def obtenir_temps_restant(joueur):
    """Retourne le temps restant pour un joueur donné"""
    if joueur == 1:
        return temps_j1
    else:
        return temps_j2