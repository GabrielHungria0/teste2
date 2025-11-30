"""Gerenciador centralizado de transições de estados do jogo."""
from patterns.state.menu_state import MenuState
from patterns.state.playing_state import PlayingState
from patterns.state.game_over_state import GameOverState


class GameStateManager:
    """Gerencia transições entre estados do jogo (Menu, Playing, GameOver)."""
    
    def __init__(self):
        """Inicializa o gerenciador com o estado inicial (Menu)."""
        self._current_state = MenuState()
    
    def get_current_state(self):
        """Retorna o estado atual."""
        return self._current_state
    
    def transition_to_menu(self):
        """Transiciona para o estado de Menu."""
        self._current_state = MenuState()
    
    def transition_to_playing(self):
        """Transiciona para o estado de Playing (jogo em andamento)."""
        self._current_state = PlayingState()
    
    def transition_to_game_over(self):
        """Transiciona para o estado de GameOver."""
        self._current_state = GameOverState()
    
    def handle_input(self, game_context, event):
        """Delega entrada para o estado atual."""
        self._current_state.handle_input(game_context, event)
    
    def update(self, game_context):
        """Delega atualização para o estado atual."""
        self._current_state.update(game_context)
    
    def render(self, game_context, screen):
        """Delega renderização para o estado atual."""
        self._current_state.render(game_context, screen)
