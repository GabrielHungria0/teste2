"""Facade para gerenciamento de estados do jogo."""


class GameStateFacade:
    """
    Facade responsável por gerenciar transições de estado do jogo.
    Encapsula o GameStateManager e fornece interface de alto nível.
    """
    
    def __init__(self, context):
        """
        Inicializa a facade de estados.
        
        Args:
            context: GameContext contendo o state_manager
        """
        self._context = context
    
    def play(self):
        """Transiciona para o estado de jogo (Playing)."""
        self._context.state_manager.transition_to_playing()
    
    def game_over(self):
        """Transiciona para o estado de game over."""
        self._context.state_manager.transition_to_game_over()
    
    def set_menu(self):
        """Transiciona para o estado de menu inicial."""
        self._context.state_manager.transition_to_menu()
