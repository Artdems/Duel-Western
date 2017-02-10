from constantes import *

def creer_map():
    carte = []
    for i in range(nb_case_longueur):
        carte.append([])
        for j in range(nb_case_hauteur):
            carte[i].append(VIDE);
    return carte
    
