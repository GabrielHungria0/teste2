"""
Arquivo principal do jogo - Game Context e Loop
"""

import pygame
from pygame.locals import QUIT

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from patterns.context import GameContext


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird Da Leila")

    game = GameContext()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            else:
                game.handle_input(event)

        game.update()
        game.render(screen)
        pygame.display.update()

    pygame.quit()
