"""Facade para gerenciamento do ciclo de vida das entidades."""
from patterns.event import ResetEvent


class EntityManagerFacade:
   
    
    def __init__(self, context):
    
        self._context = context
    
    def reset_game(self):
        self._context.event_system.notify(ResetEvent())
        self.reset_bird()
        self.reset_pipes()
    
    def reset_bird(self):
        initializer = self._context.get_initializer()
        self._context.sprite_manager.clear_group("bird")
        self._context.bird = initializer.initialize_bird(
            self._context.sprite_manager,
            self._context.resource_facade
        )
    
    def reset_pipes(self):
        initializer = self._context.get_initializer()
        self._context.sprite_manager.clear_group("pipes")
        self._context.pipe_manager = initializer.initialize_pipes(
            self._context.sprite_manager,
            self._context.resource_facade
        )
