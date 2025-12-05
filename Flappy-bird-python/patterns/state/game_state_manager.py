"""Gerenciador centralizado de transições de estados do jogo."""
from patterns.state.initial_screen_state import InitialScreenState
from patterns.state.playing_state import PlayingState
from patterns.state.game_over_state import GameOverState


class GameStateManager:
    
    def __init__(self):
        self._current_state = InitialScreenState()
    
    def get_current_state(self):
        return self._current_state
    
    def transition_to_menu(self):
        self._current_state = InitialScreenState()
    
    def transition_to_playing(self):
        self._current_state = PlayingState()
    
    def transition_to_game_over(self):
        self._current_state = GameOverState()
    
    def handle_input(self, game_context, event):
        self._current_state.handle_input(game_context, event)
    
    def update(self, game_context):
        self._current_state.update(game_context)
    
    def render(self, game_context, screen):
        self._current_state.render(game_context, screen)
