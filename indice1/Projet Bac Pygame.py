import pygame
import time
import sys


pygame.init()

# ------------------------Taille fenetre et couleur-----------------------------
screen_width = 890
screen_height = 690
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
Titre.set_underline(True)
ParaTitre = Titre.render("Gagner est votre seul échappatoire !", True, red)

Bouton = pygame.font.SysFont("arial", 15, True)
ParaBouton = Bouton.render("Espace = Accelerer  / Fleche du haut = Monter  / Fleche du bas = Descendre  / Fleche de droite = Klaxon", True, orange)

Start = pygame.font.SysFont("arial", 35, True)
Start.set_underline(True)

Bouton_Menu = pygame.font.SysFont("arial", 25, True)

End = pygame.font.SysFont("arial", 50, True)

Bouton_End = pygame.font.SysFont("arial", 25, True)

Bravo = pygame.font.SysFont("arial", 50, True)

Indice1 = pygame.font.SysFont("arial", 30, True)

# ---------------------------------Musique--------------------------------------

Bruit_De_Voiture = pygame.mixer.Sound("bruit de voiture.wav")

Klaxon = pygame.mixer.Sound("klaxon.wav")

Bruit_applaudissement = pygame.mixer.Sound("applaudissement.wav")

Bruit_de_crash = pygame.mixer.Sound("crache.wav")

# ----------------------------------objet---------------------------------------


obstacle1 = pygame.Rect(145,347,15,100)
pygame.draw.rect(screen, black, obstacle1, 5)

obstacle2 = pygame.Rect(145,547,15,100)
pygame.draw.rect(screen, black, obstacle2, 5)

obstacle3 = pygame.Rect(245,347,15,40)
pygame.draw.rect(screen, black, obstacle3, 5)

obstacle4 = pygame.Rect(245,487,15,160)
pygame.draw.rect(screen, black, obstacle4, 5)

obstacle5 = pygame.Rect(345,347,15,80)
pygame.draw.rect(screen, black, obstacle5, 5)

obstacle6 = pygame.Rect(345,527,15,120)
pygame.draw.rect(screen, black, obstacle6, 5)

obstacle7 = pygame.Rect(445,347,15,130)
pygame.draw.rect(screen, black, obstacle7, 5)

obstacle8 = pygame.Rect(445,577,15,70)
pygame.draw.rect(screen, black, obstacle8, 5)

obstacle9 = pygame.Rect(545,347,15,50)
pygame.draw.rect(screen, black, obstacle9, 5)

obstacle10 = pygame.Rect(545,487,15,160)
pygame.draw.rect(screen, black, obstacle10, 5)

obstacle11 = pygame.Rect(645,347,15,160)
pygame.draw.rect(screen, black, obstacle11, 5)

obstacle12 = pygame.Rect(645,607,15,40)
pygame.draw.rect(screen, black, obstacle12, 5)

obstacle13 = pygame.Rect(745,347,15,30)
pygame.draw.rect(screen, black, obstacle13, 5)

obstacle14 = pygame.Rect(745,447,15,200)
pygame.draw.rect(screen, black, obstacle14, 5)

pygame.display.flip()

# ----------------------------------Image---------------------------------------

route = pygame.image.load("route.png")
route.convert()

arrivee = pygame.image.load("arrivee.jpg")
arrivee.convert()
arrivee_rect= arrivee.get_rect(center=(830,347))

voiture1 = pygame.image.load("voiture1.png")
voiture1.convert()
voiture1_rect = voiture1.get_rect(center=(70,217))

voiture2 = pygame.image.load("voiture2.png")
voiture2.convert()
voiture2_rect = voiture2.get_rect(center=(70,497))

voiture3 = pygame.image.load("voiture3.jpg")
voiture3.convert()

voiture4 = pygame.image.load("voiture4.jpg")
voiture4.convert()

tete_de_mort = pygame.image.load("tete de mort.jpg")
tete_de_mort.convert()

victoire_fond = pygame.image.load("victoire_fond.jpg")
victoire_fond.convert()

cadre = pygame.image.load("cadre.png")
cadre.convert()

fond = pygame.image.load("fond.jpg")
fond.convert()

fond2 = pygame.image.load("fond2.jpg")
fond2.convert()

croix = pygame.image.load("croix.png")
croix.convert()

dossier = pygame.image.load("dossier.png")
dossier.convert()

ecran_ordi = pygame.image.load("ecran_ordi.png")
ecran_ordi.convert()

ecran_contour = pygame.image.load("ecran_contour.png")
ecran_contour.convert()

mur = pygame.image.load("mur.jpg")
mur.convert()

table = pygame.image.load("table.png")
table.convert()


# ---------------------------------Fonction-------------------------------------

def ordinateur():
    ordi = True
    while ordi:
        screen.fill(white)
        screen.blit(mur,(0,0))
        screen.blit(cadre,(135,47))
        screen.blit(table,(45,497))
        screen.blit(ecran_ordi,(245,260))
        screen.blit(dossier,(405,347))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 418 < mx < 481 and 349 < my < 435:
                    ordi = False
                    Menu()

        pygame.display.flip()


def Menu():
    point = 0
    start = Start.render("Joue Pour Gagner L'Indice !", True, red)
    bouton = True
    while bouton:
        menu.fill(white)
        screen.blit(ecran_contour,(0,0))
        screen.blit(fond,(45,47))
        screen.blit(voiture3,(55, 145))
        screen.blit(voiture4,(520, 145))
        if point == 0 :
            bouton_start = Bouton_Menu.render("Commencer", True, white)
            bouton_stop = Bouton_Menu.render("Quitter", True, black)
        elif point == 1 :
            bouton_start = Bouton_Menu.render("Commencer", True, black)
            bouton_stop = Bouton_Menu.render("Quitter", True, white)
        menu.blit(start, (230, 95))
        menu.blit(bouton_start, (365, 345))
        menu.blit(bouton_stop, (392, 405))
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
                        Bruit_De_Voiture.play()
                        return True
                    elif point == 1:
                        ordinateur()
                        bouton = False
        point = point%2
        pygame.display.flip()
    return False


def Gagner():
    victoire = True
    while victoire:
        gagner.fill(white)
        screen.blit(ecran_contour,(0,0))
        gagner.blit(victoire_fond,(45,45))
        Indice_Gagner = Indice1.render("Code : 123456789", True, orange)
        Titre_Gagner = Bravo.render("!!! Felicitation !!!", True, red)
        gagner.blit(Indice_Gagner,(305,395))
        gagner.blit(Titre_Gagner, (245,75))
        screen.blit(croix,(795,45))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                victoire = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 790 < mx < 845 and 45 < my < 85:
                    victoire = False
                    ordi = True
                    ordinateur()

def Perdu():
    perdu.fill(white)
    screen.blit(ecran_contour,(0,0))
    screen.blit(fond2,(45,47))
    Titre_Perdu = End.render("NUL GERMAIN, NUL !!!", True, white)
    perdu.blit(Titre_Perdu,(175,95))
    perdu.blit(tete_de_mort,(295,195))
    pygame.display.flip()
    time.sleep(3)
    Menu()



#Bouton de controle de la jeux
def jeux():
    ordinateur()
    voiture1_rect = voiture1.get_rect(center=(70,217))
    voiture2_rect = voiture2.get_rect(center=(70,497))
    Bruit_De_Voiture.play()
    continuer = True
    while continuer and not voiture1_rect.colliderect(arrivee_rect) and not voiture2_rect.colliderect(arrivee_rect):
        time.sleep(.100)
        screen.fill(white)
        screen.blit(ecran_contour,(0,0))
        voiture1_rect.left += 4
        screen.blit(route,(45,47))
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
        pygame.draw.line(screen, black, (45,347),(813,347), 5)
        screen.blit(ParaTitre, (190,52))
        screen.blit(ParaBouton, (63,104))
        screen.blit(croix,(795,47))
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 790 < mx < 845 and 45 < my < 85:
                    voiture1_rect = voiture1.get_rect(center=(70,217))
                    voiture2_rect = voiture2.get_rect(center=(70,497))
                    Bruit_De_Voiture.stop()
                    ordinateur()

        if voiture2_rect.x < 0 or voiture2_rect.x > screen_width or voiture2_rect.y <342 or voiture2_rect.y > 607 or voiture1_rect.colliderect(arrivee_rect) or voiture2_rect.colliderect(obstacle1)or voiture2_rect.colliderect(obstacle2)or voiture2_rect.colliderect(obstacle3) or voiture2_rect.colliderect(obstacle4) or voiture2_rect.colliderect(obstacle5) or voiture2_rect.colliderect(obstacle6) or voiture2_rect.colliderect(obstacle7) or voiture2_rect.colliderect(obstacle8) or voiture2_rect.colliderect(obstacle9) or voiture2_rect.colliderect(obstacle10) or voiture2_rect.colliderect(obstacle11) or voiture2_rect.colliderect(obstacle12) or voiture2_rect.colliderect(obstacle13) or voiture2_rect.colliderect(obstacle14):
            Bruit_De_Voiture.stop()
            Bruit_de_crash.play()
            voiture1_rect = voiture1.get_rect(center=(70,217))
            voiture2_rect = voiture2.get_rect(center=(70,497))
            Perdu()

        if voiture2_rect.colliderect(arrivee_rect):
            Bruit_applaudissement.play()
            voiture1_rect = voiture1.get_rect(center=(70,217))
            voiture2_rect = voiture2.get_rect(center=(70,497))
            Gagner()

        pygame.display.flip()
jeux()
pygame.quit()