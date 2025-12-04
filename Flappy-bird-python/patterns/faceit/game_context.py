"""Container de dados e subsistemas do jogo."""
from config import GameConfig
from initialization import GameInitializer
from patterns.state.game_state_manager import GameStateManager


class GameContext:
    """
    Container de estado do jogo (Data Container).
    Responsável APENAS por inicializar e armazenar subsistemas.
    NÃO contém lógica de negócio - apenas dados.
    """
    
    def __init__(self):
        """Inicializa o contexto e todos os subsistemas do jogo."""
        self._config = GameConfig()
        self._initializer = GameInitializer(self._config)
        
        # Inicializa todos os subsistemas
        init_dict = self._initializer.initialize_all()
        
        # Expõe subsistemas como atributos públicos
        for key, value in init_dict.items():
            setattr(self, key, value)
        
        # Gerenciador de estado (inicializado após todos os subsistemas)
        self.state_manager = GameStateManager()
        
        # Mantém referências aos helpers de inicialização
        self._initializer_ref = self._initializer
        
        # Referências para facades (acessíveis pelos estados)
        self.state_facade = None
        self.entity_facade = None
    
    def get_initializer(self):
        """Retorna o initializer para uso em resets."""
        return self._initializer_ref
