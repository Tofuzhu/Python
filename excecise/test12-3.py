import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 1024))
    pygame.display.set_caption("rocket rush")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()