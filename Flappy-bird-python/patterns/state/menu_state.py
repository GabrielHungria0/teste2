from pygame import K_SPACE, K_UP, KEYDOWN, Surface
import pygame
from config import GROUND_WIDTH
from entities.ground import Ground
from patterns.event import JumpEvent
from patterns.state.game_state import GameState
from utils.helpers import is_off_screen


class MenuState(GameState):

    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                game_context.event_system.notify(JumpEvent())
                game_context.play()

    def update(self, game_context):
        game_context.bird.begin()
        game_context.ground_group.update()

        if is_off_screen(game_context.ground_group.sprites()[0]):
            game_context.ground_group.remove(game_context.ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDTH - 20, game_context.resource_facade)
            game_context.ground_group.add(new_ground)

    def render(self, game_context, screen: Surface):
        screen.blit(game_context.background, (0, 0))
        screen.blit(game_context.begin_image, (120, 150))
        game_context.bird_group.draw(screen)
        game_context.ground_group.draw(screen)
