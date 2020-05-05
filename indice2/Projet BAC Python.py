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

table = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

gagner = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)



# -------------------------------Texte------------------------------------------


Bravo = pygame.font.SysFont("arial", 50, True)

Indice2 = pygame.font.SysFont("arial", 30, True)

# ---------------------------------Musique--------------------------------------


alarme = pygame.mixer.Sound("indice2_alarme.wav")

Bruit_applaudissement = pygame.mixer.Sound("indice1_applaudissement.wav")


# ----------------------------------objet---------------------------------------



pygame.display.flip()

# ----------------------------------Image---------------------------------------


code = pygame.image.load("indice2_code_fond.jpg")
code.convert()

table_feuille_avant1 = pygame.image.load("Indice2_table_feuille_avant1.png")
table_feuille_avant1.convert()

table_feuille_avant2 = pygame.image.load("Indice2_table_feuille_avant2.png")
table_feuille_avant2.convert()

table_feuille_arriere2 = pygame.image.load("Indice2_table_feuille_arriere2.png")
table_feuille_arriere2.convert()

fleche_gauche = pygame.image.load("indice2_fleche_gauche.jpg")
fleche_gauche.convert()

fleche_droite = pygame.image.load("indice2_fleche_droite.jpg")
fleche_droite.convert()

fleche_droite = pygame.image.load("indice2_fleche_droite.jpg")
fleche_droite.convert()

bouton = pygame.image.load("indice2_bouton.png")
bouton.convert()

tableau = pygame.image.load("indice2_tableau.png")
tableau.convert()

crayon = pygame.image.load("indice2_crayon.jpg")
crayon.convert()

chiffre_rouge = pygame.image.load("indice2_chiffre_rouge.png")
chiffre_rouge.convert()

chiffre_vert = pygame.image.load("indice2_chiffre_vert.png")
chiffre_vert.convert()


ecran = pygame.image.load("indice2_ecran.jpg")
ecran.convert()

fond = pygame.image.load("indice2_parquet.jpg")
fond.convert()

croix = pygame.image.load("indice2_croix.png")
croix.convert()

post_it = pygame.image.load("indice2_post_it.jpg")
post_it.convert()

scotch = pygame.image.load("indice2_scotch.png")
scotch.convert()

quatre = pygame.image.load("indice2_quatre.png")
quatre.convert()

cinq = pygame.image.load("indice2_cinq.jpg")
cinq.convert()

deux = pygame.image.load("indice2_deux.jpg")
deux.convert()

huit = pygame.image.load("indice2_huit.jpg")
huit.convert()

coffre = pygame.image.load("indice2_coffre.png")
coffre.convert()

coffre_ouvert = pygame.image.load("indice2_coffre_ouvert.png")
coffre_ouvert.convert()

h = pygame.image.load("indice2_h.png")
h.convert()

H = pygame.image.load("indice2_H.jpg")
H.convert()

cle = pygame.image.load("indice2_cle.png")
cle.convert()


# ---------------------------------Fonction-------------------------------------

# Trouver bouton rouge
def etape1():
    continuer1 = True
    while continuer1:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(crayon,(610,110))
        table.blit(post_it,(435,475))
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        table.blit(tableau,(220,50))
        table.blit(scotch,(450,467))
        table.blit(croix,(310,0))
        table.blit(coffre,(195,130))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 660 < mx <700 and 130 < my < 170:
                    etape2()
                    continuer1 = False
        pygame.display.flip()

# Sans la boite de crayon, on doit clicker sur le bouton rouge
def etape2():
    continuer2 = True
    while continuer2:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(post_it,(435,475))
        table.blit(scotch,(450,467))
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        table.blit(coffre,(195,130))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 660 < mx <700 and 130 < my < 170:
                    etape3()
        pygame.display.flip()

# Apres avoir appuyé sur bonton rouge, on doit trouver et retire le post-it qui cache un chiffre. Dans cette étape on a la console du milieu qui apparait.
def etape3():
    continuer4 = True
    while continuer4:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(post_it,(435,475))
        table.blit(scotch,(450,467))
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 350 < mx < 445 and 280 < my < 350:
                    alarme.stop()
                    alarme.play()
                    table.blit(croix,(310,0))
                    pygame.display.flip()
                elif 415 < mx < 465 and 455 < my < 500:
                    etape4()
        pygame.display.flip()

# Apres avoir retirer le post-it, il faut desormais taper le mot de passe. Dans cette étape se sera le premier chiffre du code
def etape4():
    continuer5 = True
    while continuer5:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 420 < mx < 440 and 280 < my < 300:
                    etape5()
                elif 350 < mx < 445 and 280 < my < 350:
                    alarme.stop()
                    alarme.play()
        pygame.display.flip()

#premier chiffre qui a était trouvé
def etape5():
    continuer6 = True
    while continuer6:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        table.blit(quatre,(305,155))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 343 < mx < 368 and 299 < my < 325:
                    etape6()
                elif 350 < mx < 445 and 280 < my < 350:
                    alarme.stop()
                    alarme.play()
        pygame.display.flip()

#Deuxieme chiffre qui a était trouvé
def etape6():
    continuer7 = True
    while continuer7:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        table.blit(cinq,(365,155))
        table.blit(quatre,(305,155))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 375 < mx < 393 and 271 < my < 296:
                    etape7()
                elif 350 < mx < 445 and 280 < my < 350:
                    alarme.stop()
                    alarme.play()
        pygame.display.flip()

#Troisième chiffre qui a était trouvé
def etape7():
    continuer8 = True
    while continuer8:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        table.blit(deux,(425,155))
        table.blit(cinq,(365,155))
        table.blit(quatre,(305,155))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 423 < mx < 448 and 299 < my < 324:
                    etape8()
                elif 350 < mx < 445 and 280 < my < 350:
                    alarme.stop()
                    alarme.play()
        pygame.display.flip()

#quatrieme chiffre qui a était trouvé, Deuxieme post-it à trouver !
def etape8():
    continuer9 = True
    while continuer9:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(post_it,(325,475))
        table.blit(scotch,(340,467))
        table.blit(huit,(485,155))
        table.blit(deux,(425,155))
        table.blit(cinq,(365,155))
        table.blit(quatre,(305,155))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 324 < mx < 365 and 475 < my < 515:
                    etape9()
        pygame.display.flip()


#Deuxieme post-it trouvé ,Mettre le bon chiffre une fois convertie en lettre
def etape9():
    continuer10 = True
    while continuer10:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant1 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_rouge,(325,250))
        table.blit(ecran,(225,140))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(huit,(485,155))
        table.blit(deux,(425,155))
        table.blit(cinq,(365,155))
        table.blit(quatre,(305,155))
        table.blit(h,(328,472))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 423 < mx < 448 and 299 < my < 324:
                    etape10()
                elif 350 < mx < 445 and 280 < my < 350:
                    alarme.stop()
                    alarme.play()
        pygame.display.flip()


# Tourner la feuille
def etape10():
    continuer11 = True
    while continuer11:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_avant2 ,(25,50))
        table.blit(fleche_droite,(745,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_vert,(325,250))
        table.blit(ecran,(225,140))
        table.blit(huit,(485,155))
        table.blit(deux,(425,155))
        table.blit(cinq,(365,155))
        table.blit(quatre,(305,155))
        table.blit(H,(245,155))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 745 < mx < 765 and 475 < my < 495:
                    etape11()
        pygame.display.flip()

# Clicker sur la signature !!
def etape11():
    continuer12 = True
    while continuer12:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_arriere2 ,(25,50))
        table.blit(fleche_gauche,(595,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        table.blit(chiffre_vert,(325,250))
        table.blit(ecran,(225,140))
        table.blit(huit,(485,155))
        table.blit(deux,(425,155))
        table.blit(cinq,(365,155))
        table.blit(quatre,(305,155))
        table.blit(H,(245,155))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 595 < mx < 620 and 475 < my < 495:
                    etape10()
                elif 595 < mx < 685 and 343 < my < 357:
                    Bruit_applaudissement.play()
                    gagner()
        pygame.display.flip()

# Victoire
def gagner():
    continuer13 = True
    while continuer13:
        table.fill(white)
        table.blit(fond ,(0,0))
        table.blit(table_feuille_arriere2 ,(25,50))
        table.blit(fleche_gauche,(595,475))
        table.blit(bouton,(660,130))
        table.blit(tableau,(220,50))
        pygame.draw.line(table, red, (293,155),(293,211), 5)
        table.blit(coffre_ouvert,(205,130))
        pygame.draw.line(table, red, (290,4),(290,45), 5)
        pygame.draw.line(table, red, (520,4),(520,45), 5)
        table.blit(cle,(370,170))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 352 < mx < 448 and 213 < my < 340:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

etape1()
pygame.quit




