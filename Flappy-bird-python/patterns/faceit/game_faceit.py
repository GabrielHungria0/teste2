"""Facade principal do jogo - compõe facades especializadas."""
from patterns.faceit.game_context import GameContext
from patterns.faceit.entity_manager_facade import EntityManagerFacade


class GameFaceit:
    """
    Facade principal do jogo (Facade of Facades).
    Compõe facades especializadas e fornece interface unificada.
    
    Responsabilidades:
    - Criar e compor as facades especializadas
    - Delegar operações para as facades apropriadas
    - Manter compatibilidade com código existente
    """
    
    def __init__(self):
        """Inicializa o contexto e todas as facades especializadas."""
        # 1. Cria o contexto (auto-inicializa subsistemas)
        self._context = GameContext()
        
        # 2. Cria as facades especializadas
        self._entity_facade = EntityManagerFacade(self._context)
        
        # 3. Injeta facades no contexto como atributos públicos
        #    Estados podem acessar via game_context.entity_facade
        self._context.entity_facade = self._entity_facade
        
        # 4. Expõe subsistemas para compatibilidade com código existente
        self._expose_context_attributes()
    
    def _expose_context_attributes(self):
        """
        Expõe atributos do contexto como atributos públicos.
        Mantém compatibilidade com código que acessa diretamente os subsistemas.
        """
        for key, value in self._context.__dict__.items():
            if not key.startswith('_'):
                setattr(self, key, value)
    
    
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
    
    
    def play(self):
        """Transiciona para o estado de jogo (Playing)."""
        self._context.state_manager.transition_to_playing()
    
    def game_over(self):
        """Transiciona para o estado de game over."""
        self._context.state_manager.transition_to_game_over()
    
    def set_menu(self):
        """Transiciona para o estado de menu inicial."""
        self._context.state_manager.transition_to_menu()
    
    # === Entity Management (delega para EntityManagerFacade) ===
    
    def reset_game(self):
        """
        Reseta o jogo completamente.
        Recria todas as entidades e atualiza referências expostas.
        """
        self._entity_facade.reset_game()
        # Re-expõe atributos que foram atualizados (bird, pipe_manager)
        self._expose_context_attributes()