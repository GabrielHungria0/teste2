"""Facade para operações do game loop."""


class GameLoopFacade:
    """
    Facade responsável pelas operações do loop principal do jogo.
    Delega input, update e render para o StateManager.
    """
    
    def __init__(self, context):
        """
        Inicializa a facade do game loop.
        
        Args:
            context: GameContext contendo os subsistemas do jogo
        """
        self._context = context
    
    def handle_input(self, event):
        """
        Processa entrada do usuário.
        
        Args:
            event: Evento pygame a ser processado
        """
        self._context.state_manager.handle_input(self._context, event)
    
    def update(self):
        """Atualiza a lógica do jogo."""
        self._context.state_manager.update(self._context)
    
    def render(self, screen):
        """
        Renderiza o estado atual do jogo.
        
        Args:
            screen: Surface do pygame onde renderizar
        """
        self._context.state_manager.render(self._context, screen)
