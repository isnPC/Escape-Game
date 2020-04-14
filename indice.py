import pygame
import time
import sys


pygame.init()

# ------------------------Taille fenetre et couleur-----------------------------
screen_width = 800
screen_height = 600
grey = (96,96,96)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
orange = (255,100,0)
jaune = (255,255,0)

menu = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

perdu = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

gagner = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
screen.fill(white)

# -------------------------------Texte------------------------------------------

Titre = pygame.font.SysFont("arial", 30, True)
ParaTitre = Titre.render("Gagner est votre seul échappatoire !", True, red)

Bouton = pygame.font.SysFont("arial", 15, True)
ParaBouton = Bouton.render("Espace = Accelerer  / Fleche du haut = Monter  / Fleche du bas = Descendre  / Fleche de droite = Klaxon", True, orange)

Start = pygame.font.SysFont("arial", 35, True)

Bouton_Menu = pygame.font.SysFont("arial", 25, True)

End = pygame.font.SysFont("arial", 50, True)

Bouton_End = pygame.font.SysFont("arial", 25, True)

Bravo = pygame.font.SysFont("arial", 50, True)

Indice1 = pygame.font.SysFont("arial", 30, True)

# ---------------------------------Musique--------------------------------------

Bruit_De_Voiture = pygame.mixer.Sound("indice1_bruit de voiture.wav")

Klaxon = pygame.mixer.Sound("indice1_klaxon.wav")

Bruit_applaudissement = pygame.mixer.Sound("indice1_applaudissement.wav")

Bruit_de_crash = pygame.mixer.Sound("indice1_crache.wav")

# ----------------------------------objet---------------------------------------


obstacle1 = pygame.Rect(100,300,15,100)
pygame.draw.rect(screen, black, obstacle1, 5)

obstacle2 = pygame.Rect(100,500,15,100)
pygame.draw.rect(screen, black, obstacle2, 5)

obstacle3 = pygame.Rect(200,300,15,40)
pygame.draw.rect(screen, black, obstacle3, 5)

obstacle4 = pygame.Rect(200,440,15,160)
pygame.draw.rect(screen, black, obstacle4, 5)

obstacle5 = pygame.Rect(300,300,15,80)
pygame.draw.rect(screen, black, obstacle5, 5)

obstacle6 = pygame.Rect(300,480,15,120)
pygame.draw.rect(screen, black, obstacle6, 5)

obstacle7 = pygame.Rect(400,300,15,130)
pygame.draw.rect(screen, black, obstacle7, 5)

obstacle8 = pygame.Rect(400,530,15,70)
pygame.draw.rect(screen, black, obstacle8, 5)

obstacle9 = pygame.Rect(500,300,15,50)
pygame.draw.rect(screen, black, obstacle9, 5)

obstacle10 = pygame.Rect(500,440,15,160)
pygame.draw.rect(screen, black, obstacle10, 5)

obstacle11 = pygame.Rect(600,300,15,160)
pygame.draw.rect(screen, black, obstacle11, 5)

obstacle12 = pygame.Rect(600,560,15,40)
pygame.draw.rect(screen, black, obstacle12, 5)

obstacle13 = pygame.Rect(700,300,15,30)
pygame.draw.rect(screen, black, obstacle13, 5)

obstacle14 = pygame.Rect(700,400,15,200)
pygame.draw.rect(screen, black, obstacle14, 5)

pygame.display.flip()

# ----------------------------------Image---------------------------------------

route = pygame.image.load("indice1_route.png")
route.convert()
route.set_alpha(100)

arrivee = pygame.image.load("indice1_arrivee.jpg")
arrivee.convert()
arrivee_rect= arrivee.get_rect(center=(785,300))

voiture1 = pygame.image.load("indice1_voiture1.jpg")
voiture1.convert()
voiture1_rect = voiture1.get_rect(center=(25,170))

voiture2 = pygame.image.load("indice1_voiture2.jpg")
voiture2.convert()
voiture2_rect = voiture2.get_rect(center=(25,450))

voiture3 = pygame.image.load("indice1_voiture3.jpg")
voiture3.convert()

voiture4 = pygame.image.load("indice1_voiture4.jpg")
voiture4.convert()

tete_de_mort = pygame.image.load("indice1_tete de mort.jpg")
tete_de_mort.convert()

drapeau1 = pygame.image.load("indice1_drapeau1.jpg")
drapeau1.convert()

drapeau2 = pygame.image.load("indice1_drapeau2.jpg")
drapeau2.convert()

# ---------------------------------Fonction-------------------------------------

def Menu():
    point = 0
    start = Start.render("Joue Pour Gagner L'Indice !", True, red)
    while 1:
        menu.fill(grey)
        screen.blit(voiture3,(0, 100))
        screen.blit(voiture4,(465, 100))
        if point == 0 :
            bouton_start = Bouton_Menu.render("Commencer", True, white)
            bouton_stop = Bouton_Menu.render("Quitter", True, black)
        elif point == 1 :
            bouton_start = Bouton_Menu.render("Commencer", True, black)
            bouton_stop = Bouton_Menu.render("Quitter", True, white)
        menu.blit(start, (185, 50))
        menu.blit(bouton_start, (310, 300))
        menu.blit(bouton_stop, (337, 360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point += 1
                elif event.key == pygame.K_UP:
                    point -=1
                elif event.key == pygame.K_RETURN:
                    if point == 0:
                        return True
                    elif point == 1:
                        pygame.quit()
                        sys.exit()
        point = point%2
        pygame.display.flip()
    return False


def Gagner():
    victoire = True
    while victoire:
        gagner.fill(jaune)
        Indice_Gagner = Indice1.render("Code : 123456789", True, orange)
        Titre_Gagner = Bravo.render("!!! Felicitation !!!", True, red)
        gagner.blit(Indice_Gagner,(260,350))
        gagner.blit(Titre_Gagner, (200,10))
        gagner.blit(drapeau2,(135,150))
        gagner.blit(drapeau1,(420,150))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                victoire = False

def Perdu():
    perdu.fill(red)
    Titre_Perdu = End.render("NUL GERMAIN, NUL !!!", True, white)
    perdu.blit(Titre_Perdu,(130,50))
    perdu.blit(tete_de_mort,(250,150))
    pygame.display.flip()
    time.sleep(3)
    jeux()

def init_voiture():
    voiture1_rect = voiture1.get_rect(center=(25,170))
    voiture2_rect = voiture2.get_rect(center=(25,450))
    screen.blit(voiture1,voiture1_rect)
    screen.blit(voiture2,voiture2_rect)
    pygame.display.flip()


#Bouton de controle de la jeux
def jeux():
    Menu()
    init_voiture()
    Bruit_De_Voiture.play()
    continuer = True
    while continuer and not voiture1_rect.colliderect(arrivee_rect) and not voiture2_rect.colliderect(arrivee_rect):
        time.sleep(.100)
        screen.fill(white)
        voiture1_rect.left += 4
        pygame.draw.rect(screen, black, obstacle1, 5)
        pygame.draw.rect(screen, black, obstacle2, 5)
        pygame.draw.rect(screen, black, obstacle3, 5)
        pygame.draw.rect(screen, black, obstacle4, 5)
        pygame.draw.rect(screen, black, obstacle5, 5)
        pygame.draw.rect(screen, black, obstacle6, 5)
        pygame.draw.rect(screen, black, obstacle7, 5)
        pygame.draw.rect(screen, black, obstacle8, 5)
        pygame.draw.rect(screen, black, obstacle9, 5)
        pygame.draw.rect(screen, black, obstacle10, 5)
        pygame.draw.rect(screen, black, obstacle11, 5)
        pygame.draw.rect(screen, black, obstacle12, 5)
        pygame.draw.rect(screen, black, obstacle13, 5)
        pygame.draw.rect(screen, black, obstacle14, 5)
        screen.blit(arrivee, arrivee_rect)
        screen.blit(voiture1,voiture1_rect)
        screen.blit(voiture2,voiture2_rect)
        screen.blit(route,(0,0))
        pygame.draw.line(screen, black, (0,300),(768,300), 5)
        screen.blit(ParaTitre, (145,5))
        screen.blit(ParaBouton, (18,57))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    voiture2_rect.x += 10
                elif event.key == pygame.K_UP:
                    voiture2_rect.y -=10
                elif event.key == pygame.K_DOWN:
                    voiture2_rect.y +=10
                elif event.key == pygame.K_RIGHT:
                    Klaxon.play()

        if voiture2_rect.x < 0 or voiture2_rect.x > screen_width or voiture2_rect.y <295 or voiture2_rect.y > 560 or voiture1_rect.colliderect(arrivee_rect) or voiture2_rect.colliderect(obstacle1)or voiture2_rect.colliderect(obstacle2)or voiture2_rect.colliderect(obstacle3) or voiture2_rect.colliderect(obstacle4) or voiture2_rect.colliderect(obstacle5) or voiture2_rect.colliderect(obstacle6) or voiture2_rect.colliderect(obstacle7) or voiture2_rect.colliderect(obstacle8) or voiture2_rect.colliderect(obstacle9) or voiture2_rect.colliderect(obstacle10) or voiture2_rect.colliderect(obstacle11) or voiture2_rect.colliderect(obstacle12) or voiture2_rect.colliderect(obstacle13) or voiture2_rect.colliderect(obstacle14):
            Bruit_De_Voiture.stop()
            Bruit_de_crash.play()
            init_voiture()
            Perdu()

        if voiture2_rect.colliderect(arrivee_rect):
            Bruit_applaudissement.play()
            Gagner()
            break

        pygame.display.flip()
jeux()
pygame.quit()
