import pygame
from constantes import *
from threading import Thread

class Controle(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self, rot1, rot2, haut, gauche, droite, bas, recharge, joueur, tick_recharge, carte):
     
        if pygame.time.get_ticks() - tick_recharge > temps_recharge and joueur.get_recharge() == True:
            joueur.recharger() 

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN and event.key == rot1:
                joueur.set_orientation(-1)
            if event.type == pygame.KEYDOWN and event.key == rot2:
                joueur.set_orientation(1)
                        
            if event.type == pygame.KEYDOWN and event.key == haut:
                joueur.deplacer(carte, HAUT)
            if event.type == pygame.KEYDOWN and event.key == gauche:
                joueur.deplacer(carte, GAUCHE)
            if event.type == pygame.KEYDOWN and event.key == droite:
                joueur.deplacer(carte, DROITE)
            if event.type == pygame.KEYDOWN and event.key == bas:
                joueur.deplacer(carte, BAS)

            if event.type == pygame.KEYDOWN and event.key == recharge and pygame.time.get_ticks() - tick_recharge > temps_recharge:
                joueur.recharger()
                tick_recharge = pygame.time.get_ticks()

        return tick_recharge
        
