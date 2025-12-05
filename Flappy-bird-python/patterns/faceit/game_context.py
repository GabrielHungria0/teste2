"""Container de dados e subsistemas do jogo."""
from config import GameConfig
from initialization import GameInitializer
from patterns.state.game_state_manager import GameStateManager


class GameContext:

    def __init__(self):
        self._config = GameConfig()
        self._initializer = GameInitializer(self._config)
        
        init_dict = self._initializer.initialize_all()
        
        for key, value in init_dict.items():
            setattr(self, key, value)
        
        self.state_manager = GameStateManager()
        
        self._initializer_ref = self._initializer
        

        self.entity_facade = None
    
    def get_initializer(self):
        return self._initializer_ref
