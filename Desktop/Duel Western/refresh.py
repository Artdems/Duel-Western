import pygame

from constantes import *



def refresh(screen, carte, joueur1, joueur2,coeur, vide, ammo, sable):

    screen.fill((255,255,255))

    for i in range (nb_case_longueur):
        for j in range (nb_case_hauteur):
            
            screen.blit(sable, (i*taille_case, j*taille_case))
            if carte[i][j] == 1 :
              screen.blit(joueur1.get_sprite(), (i*taille_case, j*taille_case))
            elif carte[i][j] == 2 :
                screen.blit(joueur2.get_sprite(), (i*taille_case, j*taille_case))

            
                
    for i in range (joueur1.get_vie()):

        screen.blit(coeur, (i*(taille_case/2), (nb_case_hauteur)*taille_case))

    if joueur1.get_vie() < 3 and joueur1.get_vie() > 0:
        for i in range (joueur1.get_vie(), 3):

            screen.blit(vide, (i*(taille_case/2), (nb_case_hauteur)*taille_case))

    for i in range (joueur1.get_ammo()):

        screen.blit(ammo, ((i+7)*(taille_case/2), (nb_case_hauteur)*taille_case))


    for i in range (joueur2.get_vie()):

        screen.blit(coeur, ((i+27)*(taille_case/2), (nb_case_hauteur)*taille_case))

    if joueur2.get_vie() < 3 and joueur2.get_vie() > 0:
        for i in range (joueur2.get_vie(), 3):

            screen.blit(vide, ((i+27)*(taille_case/2), (nb_case_hauteur)*taille_case))

    for i in range (joueur2.get_ammo()):

        screen.blit(ammo, ((i+17)*(taille_case/2), (nb_case_hauteur)*taille_case))



    pygame.display.flip()
