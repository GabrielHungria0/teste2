"""Serviço para lidar com entrada do jogador durante o jogo."""
import pygame
from patterns.decorator_.invincible_bird_decorator import InvincibleBirdDecorator
from patterns.event import JumpEvent


class InputHandler:
    """Responsável por processar entrada do jogador e executar ações correspondentes."""
    
    INVINCIBILITY_DURATION = 3.0
    
    def handle_input(self, game_context, event):
        """Processa evento de entrada."""
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(game_context, event.key)
    
    def _handle_keydown(self, game_context, key):
        """Mapeia teclas para ações de jogo."""
        if key in (pygame.K_SPACE, pygame.K_UP):
            self._handle_jump(game_context)
        elif key == pygame.K_i:
            self._activate_invincibility(game_context)
    
    def _handle_jump(self, game_context):
        """Processa pulo do pássaro."""
        game_context.bird.bump()
        game_context.event_system.notify(JumpEvent())
    
    def _activate_invincibility(self, game_context):
        """Decora o pássaro com invencibilidade temporária."""
        decorated = InvincibleBirdDecorator(
            game_context.bird, 
            duration=self.INVINCIBILITY_DURATION
        )
        game_context.bird = decorated
        game_context.sprite_manager.clear_group("bird")
        game_context.sprite_manager.add_to_group("bird", decorated)
