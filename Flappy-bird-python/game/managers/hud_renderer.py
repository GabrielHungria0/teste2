"""Gerenciador centralizado de renderização de HUD (UI)."""
import pygame
from config import GameConfig


class HUDRenderer:
    """Responsável por renderizar todos os elementos de HUD do jogo."""
    
    def __init__(self):
        self._config = GameConfig()
        self._font_large = pygame.font.Font(None, 74)
        self._font_medium = pygame.font.Font(None, 48)
        self._font_small = pygame.font.Font(None, 36)
        self._font_score = pygame.font.Font(None, 72)
    
    def render_score(self, screen, score):
        """Renderiza a pontuação em tempo real."""
        shadow = self._font_score.render(str(score), True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self._config.SCREEN_WIDTH // 2 + 3, 83))
        screen.blit(shadow, shadow_rect)
        
        text = self._font_score.render(str(score), True, (255, 255, 255))
        text_rect = text.get_rect(center=(self._config.SCREEN_WIDTH // 2, 80))
        screen.blit(text, text_rect)
    
    def render_game_over(self, screen):
        """Renderiza texto de GAME OVER."""
        text = self._font_large.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (50, 200))
    
    def render_final_score(self, screen, score):
        """Renderiza a pontuação final na tela de game over."""
        text = self._font_medium.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (120, 280))
    
    def render_restart_instructions(self, screen):
        """Renderiza instruções de reinício."""
        text = self._font_small.render("Press SPACE to restart", True, (255, 255, 255))
        screen.blit(text, (60, 350))
