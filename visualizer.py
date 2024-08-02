import pygame
import time
import os
import sys


def update(display):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Algorizer")
    check_events()
    pygame.display.update()


def keep_open(display):
    pygame.display.set_caption("Algorizer")
    while True:
        update(display)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def run():
    dimensions = [1024, 512]

    pygame.init()

    display = pygame.display.set_mode((dimensions[0], dimensions[1]))

    display.fill(pygame.Color("#a48be0"))

    try:
        keep_open(display)
        pass
    except:
        pass