import pygame
import time
import sys
import random

pygame.init()

# ------------------------Taille fenetre et couleur-----------------------------
screen_width = 800
screen_height = 600

grey = (79,93,96)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
orange = (255,100,0)
jaune = (255,255,0)
violet = (195,38,226)

screen = pygame.display.set_mode((screen_width, screen_height))



# -------------------------------Texte------------------------------------------



# ---------------------------------Musique--------------------------------------




# ----------------------------------Image---------------------------------------

piece1 = pygame.image.load("PP_piece1.jpg")
piece1.convert()

piece2 = pygame.image.load("PP_piece2.jpg")
piece2.convert()

piece3 = pygame.image.load("PP_piece3.jpg")
piece3.convert()

piece4 = pygame.image.load("PP_piece4.jpg")
piece4.convert()

piece5 = pygame.image.load("PP_piece5.jpg")
piece5.convert()

fleche1 = pygame.image.load("PP_fleche1.png")
fleche1.convert()

fleche2 = pygame.image.load("PP_fleche2.png")
fleche2.convert()

fleche3 = pygame.image.load("PP_fleche3.png")
fleche3.convert()

porte = pygame.image.load("PP_porte.png")
porte.convert()

borne = pygame.image.load("PP_borne2.png")
borne.convert()

prise = pygame.image.load("PP_prise.png")
prise.convert()

prise2 = pygame.image.load("PP_prise2.jpg")
prise2.convert()

ppchaise = pygame.image.load("PP_chaise.png")
ppchaise.convert()

ppecran = pygame.image.load("PP_ecran.png")
ppecran.convert()

deco1 = pygame.image.load("deco1.png")
deco1.convert()

deco2 = pygame.image.load("deco2.png")
deco2.convert()

deco3 = pygame.image.load("deco3.png")
deco3.convert()

deco4 = pygame.image.load("deco4.png")
deco4.convert()

prise3 = pygame.image.load("PP_prise3.png")
prise3.convert()
prise3_rect = prise3.get_rect(center = (308,520))


# ---------------------------------Fonction-------------------------------------


# Jeu
def Piece():
    jeu = True
    objet = 0
    piece = 0
    test = 0
    screen.fill(white)
    while jeu:
        if piece == 0:
            screen.blit(piece1,(0,0))
            screen.blit(fleche2,(740,275))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if 740 < mx < 790 and 275 < my < 325:
                        piece +=1
            pygame.display.flip()


        elif piece == 1:
            screen.blit(piece2,(0,0))
            screen.blit(borne,(87,175))
            screen.blit(deco1,(3,160))
            screen.blit(deco2,(275,235))
            screen.blit(deco3,(15,290))
            screen.blit(deco4,(38,370))
            screen.blit(fleche1,(10,275))
            screen.blit(fleche2,(740,275))
            screen.blit(prise2,(269,394))
            if test == 1:
                screen.blit(prise,(250,392))
                pygame.display.flip()
            else:
                screen.blit(prise3,prise3_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if 10 < mx < 60 and 275 < my < 325:
                        piece -=1
                    elif 740 < mx < 790 and 275 < my < 325:
                        piece +=1
                    elif 268 < mx < 298 and 394 < my < 418:
                        test = 1
            pygame.display.flip()

        elif piece == 2:
            screen.blit(piece3,(0,0))
            screen.blit(fleche1,(10,275))
            screen.blit(porte,(730,50))
            screen.blit(fleche2,(740,275))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    print(mx,my)
                    if 10 < mx < 60 and 275 < my < 325:
                        piece-=1
                    elif 380 < mx < 555 and 70 < my < 450:
                        piece+=1
                    elif 740 < mx < 790 and 275 < my < 325:
                        piece+=2
            pygame.display.flip()

        elif piece == 3:
            screen.blit(piece4,(0,0))
            screen.blit(fleche3,(385,540))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if 385 < mx < 425 and 540 < my < 590:
                        piece-=1
            pygame.display.flip()

        elif piece == 4:
            screen.blit(piece5,(0,0))
            screen.blit(fleche1,(10,275))
            screen.blit(ppecran,(363,288))
            screen.blit(ppchaise,(230,305))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if 10 < mx < 60 and 275 < my < 325:
                        piece-=2
            pygame.display.flip()
    clock.tick(FPS)
    pygame.display.flip()

Piece()
pygame.quit