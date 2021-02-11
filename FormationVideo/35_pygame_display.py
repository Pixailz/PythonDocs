#!/usr/bin/env python3
#coding:utf-8

"""
pygame.init()           init all modules
pygame.display.init()   init display module

pygame FLAGS:

    pygame.FULLSCREEN
          .RESIZABLE
          .NOFRAME

          .OPENGL
          .HWSURFACE
          .DOUBLEBUF
"""

import pygame

windows_resolution = 640, 480

pygame.init()

pygame.display.set_caption("35_pygame_windows.py")

window_surface = pygame.display.set_mode(windows_resolution, pygame.RESIZABLE | pygame.DOUBLEBUF)
print(type(window_surface))

print(pygame.display.Info())

sdl_version = pygame.get_sdl_version()
print(f"{sdl_version[0]}.{sdl_version[1]}.{sdl_version[2]}")

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

# THIS DO NOT CLOSE WINDOWS, UNLOAD MOD
pygame.quit()
pygame.display.init()
