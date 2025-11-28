from pygame import K_RETURN, K_SPACE, KEYDOWN
import pygame
from patterns.state import GameState
from patterns.state.menu_state import MenuState


class GameOverState(GameState):

    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_RETURN:
                game_context.reset_game()
                game_context.set_menu()

    def update(self, game_context):
        pass

    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.bird_group.draw(screen)
        game_context.pipe_group.draw(screen)
        game_context.ground_group.draw(screen)

        # Texto de Game Over
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (50, 200))

        # Pontuação final
        score = game_context.score_observer.get_score()
        font_score = pygame.font.Font(None, 48)
        text_score = font_score.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text_score, (120, 280))

        # Instruções
        font_small = pygame.font.Font(None, 36)
        text_restart = font_small.render(
            "Press SPACE to restart", True, (255, 255, 255)
        )
        screen.blit(text_restart, (60, 350))
