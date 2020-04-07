import pygame
import time

#Parametre du jeu
pygame.init()

resolution = (800, 600)
grey = (17,42,41)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)


pygame.display.set_caption("!!! Decouverte Pygame !!!")
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
screen.fill(grey)


Titre = pygame.font.SysFont("arial", 30, True)
ParaTitre = Titre.render("Découverte Pygame MG_TS4", True, red, white)
screen.blit(ParaTitre, [20,80])


objet1 = pygame.Rect(10,20,25,25)
pygame.draw.rect(screen, white, objet1, 5)
objet2 = pygame.Rect(600,10,20,200)
pygame.draw.rect(screen, black, objet2)
objet3 = pygame.Rect(10,155,25,25)
pygame.draw.rect(screen, red, objet3, 5)
pygame.display.flip()

"""arrivée = pygame.image.load("arrivée.jpg")
arrivée.convert()"""

#Bouton de controle de la fenetre
launched = True
while launched and not objet1.colliderect(objet2):
    time.sleep(.500)
    screen.fill(grey)
    objet1.x += 4
    pygame.draw.rect(screen, white, objet1, 5)
    pygame.draw.rect(screen, black, objet2)
    pygame.draw.rect(screen, red, objet3, 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                objet3.x += 5
                print("space")
    pygame.display.flip()
pygame.quit()