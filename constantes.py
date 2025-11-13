# constantes
DIMENSION_CASE = 100
NOMBRE_COLONNES = 7
NOMBRE_LIGNES = 6
RAYON = 45
DIMENSION_CONSOLE_LARGEUR = 100

DIAGONALE_1 = [(3,0),(2,1),(1,2),(0,3)]

DIAGONALE_2 = [(4,0),(3,1),(2,2),(1,3),(0,4)]

DIAGONALE_3 = [(5,0),(4,1),(3,2),(2,3),(1,4),(0,5)]

DIAGONALE_4 = [(6,0),(5,1),(4,2),(3,3),(2,4),(1,5)]

DIAGONALE_5 = [(6,1),(5,2),(4,3),(3,4),(2,5)]

DIAGONALE_6 = [(6,2),(5,3),(4,4),(3,5)]

DIAGONALE_7 = [(3,5),(2,4),(1,3),(0,2)]

DIAGONALE_8 = [(4,5),(3,4),(2,3),(1,2),(0,1)]

DIAGONALE_9 = [(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)]

DIAGONALE_10 = [(6,5),(5,4),(4,3),(3,2),(2,1),(1,0)]

DIAGONALE_11 = [(6,4),(5,3),(4,2),(3,1),(2,0)]

DIAGONALE_12 = [(6,3),(5,2),(4,1),(3,0)]

DIAGONALES = [DIAGONALE_1,DIAGONALE_2,DIAGONALE_3,DIAGONALE_4, \
    DIAGONALE_5,DIAGONALE_6,DIAGONALE_7,DIAGONALE_8, \
    DIAGONALE_9,DIAGONALE_10,DIAGONALE_11,DIAGONALE_12]

DEPART_TEXTE = (250,625)

# Liste de mots interdits pour les pseudos
MOTS_INTERDITS = [
    # Insultes courantes
    "con", "connard", "connasse", "salaud", "salope", "pute", "putain",
    "merde", "chier", "enculé", "enculer", "bite", "couille", "teub",
    "fdp", "ntm", "nique", "pd", "pédé", "taré", "débile", "crétin",
    "abruti", "idiot", "imbécile", "trou du cul", "trouduc", "cul",
    
    # Termes racistes/discriminatoires
    "negro", "négro", "bougnoule", "youpin", "bamboula", "raton",
    "crouille", "bicot", "schleu", "boche", "chintok", "chinetoque",
    
    # Termes vulgaires additionnels
    "bordel", "foutre", "salop", "connerie", "niquer", "baiser",
    "chatte", "pine", "zizi", "caca", "pipi", "sucer", "suce",
    
    # Termes offensants additionnels
    "nazi", "hitler", "facho", "fasciste", "raciste", "terroriste",
    "mort", "tuer", "suicide", "cancer", "sida",
    
    # Variantes avec chiffres
    "c0n", "s4laud", "m3rd3", "p3d3", "b1t3", "cul3",
    
    # Expressions courantes
    "va te faire", "vtf", "ta gueule", "ta mere", "ta mère",
    "ferme la", "ferme ta", "casse toi", "dégage",
    
    # Noms système réservés
    "admin", "administrateur", "system", "système", "null", "undefined",
    "bot", "ia", "ordinateur", "cpu", "npc"
]

def pseudo_est_valide(pseudo):
    """
    Vérifie si un pseudo est valide (ne contient pas de mots interdits)
    Retourne True si valide, False sinon
    """
    pseudo_lower = pseudo.lower().strip()
    
    # Vérifier si vide
    if len(pseudo_lower) == 0:
        return False
    
    # Vérifier chaque mot interdit
    for mot_interdit in MOTS_INTERDITS:
        if mot_interdit in pseudo_lower:
            return False
    
    return True