"""Facade para gerenciamento do ciclo de vida das entidades."""
from patterns.event import ResetEvent


class EntityManagerFacade:
    """
    Facade responsável pelo gerenciamento do ciclo de vida das entidades.
    Gerencia reset e recriação de entidades do jogo.
    """
    
    def __init__(self, context):
        """
        Inicializa a facade de gerenciamento de entidades.
        
        Args:
            context: GameContext contendo as entidades e subsistemas
        """
        self._context = context
    
    def reset_game(self):
        """
        Reseta o jogo completamente.
        Notifica evento de reset e recria todas as entidades.
        """
        self._context.event_system.notify(ResetEvent())
        self.reset_bird()
        self.reset_pipes()
    
    def reset_bird(self):
        """Reseta o pássaro à posição inicial."""
        initializer = self._context.get_initializer()
        self._context.sprite_manager.clear_group("bird")
        self._context.bird = initializer.initialize_bird(
            self._context.sprite_manager,
            self._context.resource_facade
        )
    
    def reset_pipes(self):
        """Reseta os pipes."""
        initializer = self._context.get_initializer()
        self._context.sprite_manager.clear_group("pipes")
        self._context.pipe_manager = initializer.initialize_pipes(
            self._context.sprite_manager,
            self._context.resource_facade
        )
