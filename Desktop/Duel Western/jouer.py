# -*- coding: cp1252 -*-
import pygame
import threading 

from constantes import *
from carte import *
from CowBoy import *
from refresh import *
from pygame.locals import *


def jouer(screen):

    running = True

    carte = creer_map()
    
    bas = pygame.image.load('image/bas.png').convert()
    recharge = pygame.image.load('image/recharge.png').convert()
    tirer = pygame.image.load('image/tire.png').convert()
    toucher = pygame.image.load('image/touche.png').convert()
    coeur = pygame.image.load('image/coeur.png').convert()
    vide = pygame.image.load('image/coeurBriser.png').convert()
    ammo = pygame.image.load('image/ammo.png').convert()

    pygame.mixer.music.load("song/musique.mp3")
    pygame.mixer.music.queue("song/musique.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    feu = pygame.mixer.Sound("song/tir.wav")
    rech = pygame.mixer.Sound("song/recharge.wav")
    ouch = pygame.mixer.Sound("song/ouch.wav")
    charg = pygame.mixer.Sound("song/vide.wav")




    joueur1 = CowBoy(carte, bas, recharge,tirer,toucher, 0, 0, 1)
    j1tick = [ temps_recharge, temps_tir, temps_recharge]


    joueur2 = CowBoy(carte, bas, recharge,tirer,toucher, 0, 1, 2)
    j2tick = [ temps_recharge, temps_tir, temps_recharge]


    while running:

        j1tick = ticks_end(joueur1, j1tick)
        j2tick = ticks_end(joueur2, j2tick)
        '''if pygame.time.get_ticks() - j1_recharge > temps_recharge and joueur1.get_recharge() == True:
            joueur1.recharger()

        if pygame.time.get_ticks() - j1_tir > temps_tir and joueur1.get_tir() == True:
            joueur1.tir = False

        if pygame.time.get_ticks() - j1_touche > temps_recharge and joueur1.get_touche() == True:
            joueur1.toucher(joueur1)

        if pygame.time.get_ticks() - j2_recharge > temps_recharge and joueur2.get_recharge() == True:
            joueur2.recharger()

        if pygame.time.get_ticks() - j2_tir > temps_tir and joueur2.get_tir() == True:
            joueur2.tir = False

        if pygame.time.get_ticks() - j2_touche > temps_recharge and joueur2.get_touche() == True:
            joueur2.toucher(joueur2)'''


        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                
            j1tick = controles(K_q, K_e, K_w, K_a, K_d, K_s, K_r, K_SPACE, joueur1, j1tick, carte, event, joueur2, feu, rech, ouch, charg)
            j2tick = controles(K_u, K_o, K_i, K_j, K_l, K_k, K_p, K_RETURN, joueur2, j2tick, carte, event, joueur1, feu, rech, ouch, charg)


        refresh(screen, carte, joueur1, joueur2,coeur, vide, ammo)
                                 


def controles(rot1, rot2, haut, gauche, droite, bas, recharge, tir, joueur, tick, carte, event, ennemi, feu, rech, ouch, charg):

    touche = False
     
    

    
        
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

    if event.type == pygame.KEYDOWN and event.key == recharge and pygame.time.get_ticks() - tick[0] > temps_recharge:
        rech.play()
        joueur.recharger()
        tick[0] = pygame.time.get_ticks()

    if event.type == pygame.KEYDOWN and event.key == tir and pygame.time.get_ticks() - tick[1] > temps_tir and joueur.balles > 0 and joueur.balles > 0:
        feu.play()
        touche = joueur.tirer(carte, joueur)
        tick[1] = pygame.time.get_ticks()

    elif event.type == pygame.KEYDOWN and event.key == tir and joueur.balles == 0:
        charg.play()

    if touche == True and pygame.time.get_ticks() - tick[2] > temps_recharge:
        ouch.play()
        ennemi.toucher(ennemi)
        tick[2] = pygame.time.get_ticks()

    return tick


def ticks_end(joueur, tick):
    if pygame.time.get_ticks() - tick[0] > temps_recharge and joueur.get_recharge() == True:
            joueur.recharger()

    if pygame.time.get_ticks() - tick[1] > temps_tir and joueur.get_tir() == True:
        joueur.tir = False

    if pygame.time.get_ticks() - tick[2] > temps_recharge and joueur.get_touche() == True:
        joueur.toucher(joueur)

    return tick
        

        
        
        
