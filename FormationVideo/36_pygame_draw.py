#!/usr/bin/env python3
#coding:utf-8

import pygame

pygame.init()

window_resolution = (640, 480)
#BLUE = (0, 255, 255)
BLUE = (89, 152, 255)
BLACK = (0, 0, 0)
EPAISSEUR = 2

pygame.display.set_caption("36_pygame_surface.py")

window_surface = pygame.display.set_mode(size=window_resolution)
window_surface.fill(color=BLUE)

pygame.draw.line(surface=window_surface, color=BLACK, start_pos=(15,15), end_pos=(25,55), width=EPAISSEUR)

rectangle = pygame.Rect(50, 10, 50, 150)
pygame.draw.rect(surface=window_surface, color=BLACK, rect=rectangle)

rectangle = pygame.Rect(102, 10, 50, 150)
pygame.draw.rect(surface=window_surface, color=BLACK, rect=rectangle, width=EPAISSEUR)

pygame.draw.circle(surface=window_surface, color=BLACK, center=(220, 60), radius=50, width=EPAISSEUR)

polygon = [(300, 50), (350, 50), (350, 100), (300, 100)]
pygame.draw.polygon(surface=window_surface, color=BLACK, points=polygon, width=EPAISSEUR)

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
