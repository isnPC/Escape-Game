import pygame
import time
import sys

pygame.init()
screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

import indice1.indice1


# ------------------------Taille fenetre et couleur-----------------------------

indice1.indice1.jeux(screen)

pygame.quit()