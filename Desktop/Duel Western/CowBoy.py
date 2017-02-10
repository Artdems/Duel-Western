import pygame

from constantes import *

class CowBoy:
    def __init__(self, carte, bas, recharge,tirer,toucher, x, y, num):
        self.sprite_pg = bas
        self.sprite_recharge = recharge
        self.sprite_tir = tirer
        self.sprite_touche = toucher
        
        self.recharge = True
        self.tir = False
        self.touche = False
        
        self.orientation = BAS
        self.case_x = x
        self.case_y = y

        self.numero = num

        carte[x][y] = self.numero

        self.balles = 6
        self.vie = 3

    def get_sprite(self):
        if self.recharge == False and self.tir == False and self.touche == False:
            ret = self.sprite_pg
        elif self.tir == True:
            ret = self.sprite_tir
        elif self.touche == True:
            ret = self.sprite_touche
        else:
            ret = self.sprite_recharge
            
        if(self.orientation == HAUT):
            ret = pygame.transform.rotate(ret, 180)
        elif(self.orientation == GAUCHE):
            ret = pygame.transform.rotate(ret, -90)
        elif(self.orientation == DROITE):
            ret = pygame.transform.rotate(ret, 90)

        return ret

    def get_vie(self):
        return self.vie

    def get_ammo(self):
        return self.balles

    def get_case(self):
        return [self.case_x, self.case_y]
    
    def deplacer(self, carte, direction):
        if self.recharge == False:
            x = self.case_x
            y = self.case_y

            if direction == HAUT:
                y -= 1
            elif direction == BAS:
                y += 1
            elif direction == GAUCHE:
                x -= 1
            elif direction == DROITE:
                x += 1
            
            if(x >= 0 and x < nb_case_longueur and y >= 0 and y < nb_case_hauteur and carte[x][y] == VIDE):
                carte[self.case_x][self.case_y] = VIDE
                self.case_x = x
                self.case_y = y
                
                carte[self.case_x][self.case_y] = self.numero
            
    def set_orientation(self, o):
        self.orientation += o
        if (self.orientation > DROITE):
            self.orientation = BAS
        elif (self.orientation < BAS):
            self.orientation = DROITE

    def recharger(self):
        if self.recharge == False:
            self.recharge = True
        else:
            self.recharge = False
            self.balles = 6

    def get_recharge(self):
        return self.recharge

    def get_tir(self):
        return self.tir

    def tirer(self, carte, joueur):
        self.tir = True
        touche = False
        if self.balles > 0:
            self.balles -= 1
            tab = [0,0]
            continuer = True
            x =self.case_x
            y = self.case_y
            if self.orientation == HAUT:
                tab[0] = 0
                tab[1] = -1
            elif self.orientation == BAS:
                tab[0] = 0
                tab[1] = 1
            elif self.orientation == GAUCHE:
                tab[0] = -1
                tab[1] = 0
            elif self.orientation == DROITE:
                tab[0] = 1
                tab[1] = 0

            x+= tab[0]
            y+= tab[1]

            while continuer:
                if x >= 0 and x<nb_case_longueur and y>=0 and y<nb_case_hauteur and carte[x][y] != VIDE:
                    continuer = False
                    if carte[x][y] != OBSTACLE:
                        touche = True
                else:
                    x+= tab[0]
                    y+= tab[1]

                if x < 0 or x>=nb_case_longueur or y<0 or y>=nb_case_hauteur:
                    continuer = False

            return touche

    def toucher(self,joueur):
        if self.touche == False:
            self.touche = True
            print "toucher"
            joueur.degats()
        else:
            self.touche = False

    def get_touche(self):
        return self.touche

    def degats(self):
        self.vie -= 1
        if self.vie == 0:
            print "Le jouer ", self.numero, " est mort !!"
                
            

        

        
        
        
