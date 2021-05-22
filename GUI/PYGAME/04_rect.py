#!/usr/bin/env python3
#coding:utf-8

"""
pygame.Rect(x, y, widh, height)

pygame.Rect.
           .copy()
           .move() | .move_ip()
           .inflate()
           .colliderect()
"""

import pygame
import time

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 75, 255)
i = 0

pygame.init()
window_resolution = (640, 480)

pygame.display.set_caption("38_pygame_rect.py")
window_surface = pygame.display.set_mode(window_resolution)

myrect = pygame.Rect(10, 100, 25, 25)
myblock = pygame.Rect(600, 50, 20, 300)
pygame.draw.rect(surface=window_surface, color=RED, rect=myrect)
pygame.draw.rect(surface=window_surface, color=BLUE, rect=myblock)
pygame.display.flip()

"""
while i < 100:
    time.sleep(0.05)
    window_surface.fill(BLACK)
    myrect.x += 1
    myrect.y += 1
    pygame.draw.rect(window_surface, RED, myrect)
    pygame.display.flip()
    i += 1
"""

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    while not myrect.colliderect(myblock):

        time.sleep(0.005)
        window_surface.fill(BLACK)
        myrect.x += 1
        pygame.draw.rect(surface=window_surface, color=BLUE, rect=myblock)
        pygame.draw.rect(surface=window_surface, color=RED, rect=myrect)
        pygame.display.flip()
