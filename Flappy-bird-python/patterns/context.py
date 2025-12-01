import pygame
from config import GameConfig
from patterns.event import ResetEvent
from patterns.initialization import GameInitializer, GameInitializationService
from patterns.state.game_state_manager import GameStateManager


class GameContext:
    """
    Orquestrador centralizado do jogo (Facade).
    Fornece acesso unificado a subsistemas, mas delega inicialização.
    """
    
    def __init__(self):
        self._config = GameConfig()
        self._initializer = GameInitializer()
        self._init_service = GameInitializationService(self._config, self._initializer)
        
        # Inicializa todos os subsistemas
        init_dict = self._init_service.initialize_all()
        
        # Expõe subsistemas como atributos públicos
        for key, value in init_dict.items():
            setattr(self, key, value)
        
        # Gerenciador de estado (inicializado após todos os subsistemas)
        self._state_manager = GameStateManager()

    def handle_input(self, event):
        """Delega entrada ao estado atual."""
        self._state_manager.handle_input(self, event)

    def update(self):
        """Delega atualização ao estado atual."""
        self._state_manager.update(self)

    def render(self, screen):
        """Delega renderização ao estado atual."""
        self._state_manager.render(self, screen)

    def play(self):
        """Transiciona para estado de jogo."""
        self._state_manager.transition_to_playing()

    def game_over(self):
        """Transiciona para estado de game over."""
        self._state_manager.transition_to_game_over()

    def set_menu(self):
        """Transiciona para estado de menu."""
        self._state_manager.transition_to_menu()

    def reset_game(self):
        """Reseta o jogo (event + entidades)."""
        self.event_system.notify(ResetEvent())
        self._reset_bird()
        self._reset_pipes()

    def _reset_bird(self):
        """Reseta o pássaro à posição inicial."""
        self.sprite_manager.clear_group("bird")
        self.bird = self._initializer.initialize_bird(self.sprite_manager, self.resource_facade)

    def _reset_pipes(self):
        """Reseta os pipes."""
        self.sprite_manager.clear_group("pipes")
        self.pipe_manager = self._initializer.initialize_pipes(self.sprite_manager, self.resource_facade)