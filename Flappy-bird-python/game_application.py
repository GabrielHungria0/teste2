import pygame
from pygame.locals import QUIT
from config import GameConfig
from patterns.faceit.game_context import GameContext
from patterns.faceit.entity_manager_facade import EntityManagerFacade


class GameApplication:
    def __init__(self):
        self._config = GameConfig()
        self._initialize_pygame()
        self._setup_display()
        
        self._game_context = GameContext()
        self._entity_facade = EntityManagerFacade(self._game_context)
        self._game_context.entity_facade = self._entity_facade
        
        self._clock = pygame.time.Clock()
    
    def _initialize_pygame(self):
        pygame.init()
        pygame.mixer.init()
    
    def _setup_display(self):
        self._screen = pygame.display.set_mode(
            (self._config.SCREEN_WIDTH, self._config.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Flappy Bird")
    
    def run(self):
        running = True
        while running:
            running = self._process_frame()
        pygame.quit()
    
    def _process_frame(self):
        self._clock.tick(20)
        
        if not self._handle_events():
            return False
        
        self._game_context.state_manager.update(self._game_context)
        self._game_context.state_manager.render(self._game_context, self._screen)
        pygame.display.update()
        return True
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            self._game_context.state_manager.handle_input(self._game_context, event)
        return True