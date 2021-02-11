#!/usr/bin/env python3
#coding:utf-8

"""
pygame.image.load() retourne une surface

RGB (RED, GREEN, BLUE)
RGBa(RED, GREEN, BLUE, ALPHA)
"""

import pygame

pygame.init()
window_resolution = (800, 600)
BLACK = (0, 0, 0)
BLANK = (255, 255, 255)

pygame.display.set_caption("37_pygame_pictures.py")
window_surface = pygame.display.set_mode(window_resolution)

cat1 = pygame.image.load("cat.jpg")
cat1.convert() # SANS TRANSPARENCE

cat2 = pygame.image.load("cat.png")
cat2.convert_alpha() # AVEC TRANSPARENCE

cat3 = pygame.image.load("cat.jpg")
cat3.convert()
cat3.set_colorkey(BLANK) # MET EN TRANSPARENT LA COULEUR VOULU

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    # Corps du programme
    #window_surface.fill(color=BLANK)
    window_surface.fill(color=BLACK)
    window_surface.blit(source=cat1, dest=(0, 0))
    window_surface.blit(source=cat2, dest=(0, 0))
    window_surface.blit(source=cat3, dest=(0, 0))
    pygame.display.flip()
