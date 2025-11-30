import pygame
from config import GameConfig


class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize, resource_facade):
        pygame.sprite.Sprite.__init__(self)
        
        self._config = GameConfig()
        self._inverted = inverted
        self.pair_id = None
        
        self._setup_image(resource_facade)
        self._setup_position(xpos, ysize)
    
    def _setup_image(self, resource_facade):
        self.image = resource_facade.get_image("pipe")
        self.image = pygame.transform.scale(
            self.image, 
            (self._config.PIPE_WIDTH, self._config.PIPE_HEIGHT)
        )
        
        if self._inverted:
            self.image = pygame.transform.flip(self.image, False, True)
        
        self.mask = pygame.mask.from_surface(self.image)
    
    def _setup_position(self, xpos, ysize):
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = self._calculate_y_position(ysize)
    
    def _calculate_y_position(self, ysize):
        if self._inverted:
            return -(self.rect[3] - ysize)
        return self._config.SCREEN_HEIGHT - ysize
    
    def update(self):
        """Atualiza a posição horizontal do pipe (movimento)."""
        self._move_horizontal()
    
    def _move_horizontal(self):
        """Move o pipe para a esquerda na velocidade do jogo."""
        self.rect[0] -= self._config.GAME_SPEED