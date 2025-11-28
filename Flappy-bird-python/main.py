"""
Arquivo principal do jogo - Game Context e Loop
"""
import pygame
from pygame.locals import QUIT

from config import SCREEN_WIDHT, SCREEN_HEIGHT, GROUND_WIDHT
from entities.bird import Bird
from entities.ground import Ground
from patterns.facade import ResourceFacade
from patterns.observer import GameEventSubject, ScoreObserver, SoundObserver
from patterns.factory import PipeFactory
from patterns.state import MenuState



class GameContext:
    """Contexto que gerencia o estado atual do jogo"""
    
    def __init__(self):
        # Sistema de eventos (Observer)
        self.event_system = GameEventSubject()
        self.score_observer = ScoreObserver()
        self.sound_observer = SoundObserver()
        self.event_system.attach(self.score_observer)
        self.event_system.attach(self.sound_observer)
        
        # Facade de recursos (carrega UMA vez)
        self.resource_facade = ResourceFacade()
        
        # Factory de obstáculos
        self.obstacle_factory = PipeFactory()
        
        # Recursos visuais
        self.background = self.resource_facade.get_scaled_background(SCREEN_WIDHT, SCREEN_HEIGHT)
        self.begin_image = self.resource_facade.get_image('message')
        
        # Grupos de sprites
        self.bird_group = pygame.sprite.Group()
        self.bird = Bird(self.resource_facade)
        self.bird_group.add(self.bird)
        
        self.ground_group = pygame.sprite.Group()
        for i in range(2):
            ground = Ground(GROUND_WIDHT * i, self.resource_facade)
            self.ground_group.add(ground)
        
        self.pipe_group = pygame.sprite.Group()
        for i in range(2):
            pipes = self.obstacle_factory.create_obstacle(SCREEN_WIDHT * i + 800, self.resource_facade)
            self.pipe_group.add(pipes[0])
            self.pipe_group.add(pipes[1])
        
        # Estado inicial
        self._state = MenuState()
    
    def set_state(self, state):
        """Muda o estado do jogo"""
        self._state = state
    
    def handle_input(self, event):
        """Delega input para o estado atual"""
        self._state.handle_input(self, event)
    
    def update(self):
        """Atualiza o estado atual"""
        self._state.update(self)
    
    def render(self, screen):
        """Renderiza o estado atual"""
        self._state.render(self, screen)
    
    def reset_game(self):
        """Reinicia o jogo"""
        # Reseta pontuação
        self.event_system.notify("RESET")
        
        # Reseta factory para pipes normais
        self.obstacle_factory = PipeFactory()
        
        # Reseta pássaro
        self.bird_group.empty()
        self.bird = Bird(self.resource_facade)
        self.bird_group.add(self.bird)
        
        # Reseta pipes
        self.pipe_group.empty()
        for i in range(2):
            pipes = self.obstacle_factory.create_obstacle(SCREEN_WIDHT * i + 800, self.resource_facade)
            self.pipe_group.add(pipes[0])
            self.pipe_group.add(pipes[1])
    


def main():
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird Da Leila')
    
    game = GameContext()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(15)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            else:
                game.handle_input(event)
        
        game.update()
        game.render(screen)
        pygame.display.update()
    
    pygame.quit()


if __name__ == '__main__':
    main()