import pygame
import time
import sys
import random

pygame.init()

# ------------------------Taille fenetre et couleur-----------------------------
screen_width1 = 699
screen_height1 = 785

screen_width2 = 699
screen_height2 = 785

grey = (79,93,96)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
orange = (255,100,0)
jaune = (255,255,0)
violet = (195,38,226)

arcade1 = pygame.display.set_mode((screen_width1, screen_height1))

arcade2 = pygame.display.set_mode((screen_width2, screen_height2))

deplacement = 3

FPS = 30

position_tireY = 310


clock = pygame.time.Clock()


# -------------------------------Texte------------------------------------------


Score = pygame.font.SysFont("arial", 25, True)


# ---------------------------------Musique--------------------------------------


estomac = pygame.mixer.Sound("indice3_estomac.wav")

punch = pygame.mixer.Sound("indice3_punch.wav")

rire = pygame.mixer.Sound("indice3_rire.wav")

attente = pygame.mixer.Sound("indice3_attente.wav")

pacman = pygame.mixer.Sound("indice3_pacman.wav")

deplacement1 = pygame.mixer.Sound("indice3_deplacement.wav")

# ----------------------------------Image---------------------------------------


borne = pygame.image.load("indice3_borne.png")
borne.convert()

fond1 = pygame.image.load("indice3_fond1.jpg")
fond1.convert()

fond2 = pygame.image.load("indice3_arcade_fond.jpg")
fond2.convert()

fond3 = pygame.image.load("indice3_fond3.jpg")
fond3.convert()

deco1 = pygame.image.load("indice3_deco1.jpg")
deco1.convert()

deco2 = pygame.image.load("indice3_deco2.jpg")
deco2.convert()

deco3 = pygame.image.load("indice3_deco3.jpg")
deco3.convert()

deco4 = pygame.image.load("indice3_deco4.jpg")
deco4.convert()

sol = pygame.image.load("indice3_sol.jpg")
sol.convert()

bouton_start = pygame.image.load("indice3_bouton_start.png")
bouton_start.convert()

ecran1 = pygame.image.load("indice3_ecran1.png")
ecran1.convert()

ecran2 = pygame.image.load("indice3_ecran2.png")
ecran2.convert()

ecran3 = pygame.image.load("indice3_ecran3.png")
ecran3.convert()

borne_contour = pygame.image.load("indice3_contour_borne.png")
borne_contour.convert()

panel = pygame.image.load("indice3_panel3.png")
panel.convert()

top = pygame.image.load("indice3_top.jpg")
top.convert()

cadre = pygame.image.load("indice3_cadre.png")
cadre.convert()

cadre2 = pygame.image.load("indice3_cadre2.png")
cadre2.convert()

carte = pygame.image.load("indice3_carte.png")
carte.convert()

boite = pygame.image.load("indice3_boite.jpg")
boite.convert()

stickers = pygame.image.load("indice3_stickers.png")
stickers.convert()

pizza = pygame.image.load("indice3_pizza.png")
pizza.convert()
pizza_rect = pizza.get_rect(center=(random.randrange(700, 1500, deplacement), random.randrange(130, 600, deplacement)))

perso = pygame.image.load("indice3_perso.png")
perso.convert()
perso_rect = perso.get_rect(center=(100,position_tireY))

fantome = pygame.image.load("indice3_fantome.png")
fantome.convert()
fantome_rect = fantome.get_rect(center=(random.randrange(700, 1000, deplacement), random.randrange(130, 600, deplacement)))

rond = pygame.image.load("indice3_rond.png")
rond.convert()
rond_rect = rond.get_rect(center=(140,perso_rect.y + 30))

camion = pygame.image.load("indice3_camion.png")
camion.convert()
camion_rect = camion.get_rect(center=(random.randrange(700, 3000, deplacement), random.randrange(130, 600, deplacement)))

# ---------------------------------Fonction-------------------------------------

# Page d'acceuil et démarage du jeu
def etape1():
    continuer1 = True
    while continuer1:
        arcade1.fill(white)
        arcade1.blit(fond1,(0,0))
        arcade1.blit(sol,(0,650))
        arcade1.blit(borne,(128,0))
        arcade1.blit(ecran1,(221,160))
        arcade1.blit(deco1,(10,10))
        arcade1.blit(deco2,(510,150))
        arcade1.blit(deco3,(30,250))
        arcade1.blit(deco4,(90,400))
        arcade1.blit(bouton_start,(315,418))
        arcade1.blit(cadre2,(310,160))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                print(mx,my)
                if 320 < mx < 355 and 426 < my < 456:
                    attente.play()
                    etape2()
        pygame.display.flip()

# Debut du jeu : ENTER
def etape2():
    continuer2 = True
    while continuer2:
        arcade1.fill(grey)
        arcade1.blit(top,(-50,-90))
        arcade1.blit(fond2,(10,78))
        arcade1.blit(ecran2,(0,68))
        arcade1.blit(panel,(-34,655))
        arcade1.blit(cadre,(222,67))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    attente.stop()
                    pacman.play()
                    etape3()
        pygame.display.flip()

# Jeu
def etape3():
    points = 0
    continuer2 = True
    perso_rect = perso.get_rect(center=(100,310))
    pizza_rect = pizza.get_rect(center=(random.randrange(700, 1500, deplacement), random.randrange(130, 600, deplacement)))
    fantome_rect = fantome.get_rect(center=(random.randrange(700, 1000, deplacement), random.randrange(130, 600, deplacement)))
    rond_rect = rond.get_rect(center=(140,perso_rect.y + 30))
    camion_rect = camion.get_rect(center=(random.randrange(700, 3000, deplacement), random.randrange(130, 600, deplacement)))
    direction = 0
    tire = 0
    angle = 0

    while continuer2:
        arcade1.fill(grey)
        arcade1.blit(top,(-50,-90))
        arcade1.blit(fond3,(50,100))
        pygame.draw.line(arcade1, violet, (145,120),(145,625), 5)
        arcade1.blit(perso,perso_rect)
        arcade1.blit(pizza,pizza_rect)
        arcade1.blit(fantome,fantome_rect)
        arcade1.blit(camion,camion_rect)
        arcade1.blit(ecran3,(0,68))
        arcade1.blit(panel,(-34,655))
        arcade1.blit(cadre,(222,67))
        if points >= 30:
                victoire()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = -1
                    deplacement1.stop()
                    deplacement1.play()
                elif event.key == pygame.K_DOWN:
                    direction = 1
                    deplacement1.stop()
                    deplacement1.play()
                elif event.key == pygame.K_RIGHT:
                    direction = 0
                elif event.key == pygame.K_SPACE:
                    rond_rect = rond.get_rect(center=(140,perso_rect.y + 30))
                    tire = 1

        # Condition pour le deplacement du personnage
        if direction == -1 and perso_rect.y > 126:
            perso_rect.y -= deplacement
        elif direction == 1 and perso_rect.y < 575:
            perso_rect.y += deplacement
        else:
            direction == 0


        # Condition pour le deplacement de la balle et si le tire atteint sa cible
        if tire == 1:
            angle += 6
            arcade1.blit(pygame.transform.rotate(rond,angle),rond_rect)
            rond_rect.x += deplacement
            rond_rect.y += 0
        if rond_rect.colliderect(fantome_rect):
            fantome_rect = fantome.get_rect(center=(random.randrange(700, 1000, deplacement), random.randrange(130, 600, deplacement)))
            punch.play()
            tire = 0
        if rond_rect.x > 700:
            tire = 0

        # Deplacement de la pizza, du camion et du fantome
        pizza_rect.x -= deplacement
        fantome_rect.x -= deplacement
        camion_rect.x -=deplacement

        # Condition pour la pizza si elle se fait manger ou non
        if pizza_rect.x <= 0:
            pizza_rect = pizza.get_rect(center=(random.randrange(700, 1500, deplacement), random.randrange(130, 600, deplacement)))
        if perso_rect.colliderect(pizza_rect):
            points += 1
            pizza_rect = pizza.get_rect(center=(random.randrange(700, 1500, deplacement), random.randrange(130, 600, deplacement)))
            estomac.play()

        # Condition pour si le camion se fait manger ou non
        if camion_rect.x <= 0:
            camion_rect = camion.get_rect(center=(random.randrange(700, 3000, deplacement), random.randrange(130, 600, deplacement)))
        if perso_rect.colliderect(camion_rect):
            points += 3
            camion_rect = camion.get_rect(center=(random.randrange(700, 3000, deplacement), random.randrange(130, 600, deplacement)))
            estomac.play()

        # Condition si le fantome atteint le personnage
        if fantome_rect.x <= 145 or perso_rect.colliderect(fantome_rect):
            fantome_rect = fantome.get_rect(center=(random.randrange(700, 1000, deplacement), random.randrange(130, 600, deplacement)))
            rire.play()
            points -= 2

        # Score qui s'affiche
        texte = Score.render("Score : " + str(points) + " / 30", True, white)
        arcade1.blit(texte,(267,77))

        #Limite du jeu pour le personnage
        limite()

        clock.tick(FPS)
        pygame.display.flip()


def limite():
    perso_rect = perso.get_rect(center=(100,position_tireY))
    if perso_rect.y <= 125:
        perso_rect = perso.get_rect(center=(100,position_tireY))
    elif perso_rect.y >= 619:
        perso_rect -= deplacement

def victoire():
    continuer1 = True
    while continuer1:
        arcade1.fill(white)
        arcade1.blit(fond1,(0,0))
        arcade1.blit(sol,(0,650))
        arcade1.blit(borne,(128,0))
        arcade1.blit(ecran1,(221,160))
        arcade1.blit(deco1,(10,10))
        arcade1.blit(deco2,(510,150))
        arcade1.blit(deco3,(30,250))
        arcade1.blit(deco4,(90,400))
        arcade1.blit(bouton_start,(315,418))
        arcade1.blit(cadre2,(310,160))
        arcade1.blit(boite,(275,630))
        arcade1.blit(carte,(285,615))
        arcade1.blit(stickers,(255,175))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 320 < mx < 355 and 426 < my < 456:
                    attente.play()
                    etape2()
        pygame.display.flip()


etape1()
pygame.quit