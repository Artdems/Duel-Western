# -*- coding: cp1252 -*-
import sys, pygame, os
from constantes import *
from jouer import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((taille_case*nb_case_longueur, taille_case*(nb_case_hauteur+1)))
jouer(screen)
pygame.display.quit()

