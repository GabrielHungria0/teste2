import pygame
from patterns.state.game_state import GameState
from patterns.service.input_handler import InputHandler
from patterns.service.gameplay_service import GameplayService


class PlayingState(GameState):
    """Estado de jogo em andamento: orquestra input, lógica de jogo e renderização."""
    
    def __init__(self):
        self._input_handler = InputHandler()
        self._gameplay_service = GameplayService()
    
    def handle_input(self, game_context, event):
        """Delega entrada para o InputHandler."""
        self._input_handler.handle_input(game_context, event)
    
    def update(self, game_context):
        """Delega lógica de jogo para o GameplayService."""
        self._gameplay_service.update(game_context)
    
    def render(self, game_context, screen):
        """Renderiza o estado visual do jogo."""
        screen.blit(game_context.background, (0, 0))
        game_context.sprite_manager.draw_group("bird", screen)
        game_context.sprite_manager.draw_group("pipes", screen)
        game_context.sprite_manager.draw_group("ground", screen)
        
        score = game_context.score_observer.get_score()
        game_context.hud_renderer.render_score(screen, score)