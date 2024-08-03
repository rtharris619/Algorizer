import pygame
import random

from DrawInformation import DrawInformation

pygame.init()


def main():

    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 1
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(pygame, 800, 600, lst)

    while run:
        clock.tick(60)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        lst.append(random.randint(min_val, max_val))

    return lst


if __name__ == "__main__":
    main()
