import time
import pygame
from config import GameConfig
from game.collision import DecoratorAwareCollisionDetector
from patterns.decorator import InvincibleBirdDecorator
from game.difficulty import DifficultyManager
from patterns.event import CollisionEvent, GameOverEvent, JumpEvent, PipePassedEvent
from patterns.state.game_state import GameState


class PlayingState(GameState):
    def __init__(self):
        self._config = GameConfig()
        self._difficulty_manager = DifficultyManager()
        self._collision_detector = DecoratorAwareCollisionDetector()
        self._font = pygame.font.Font(None, 72)
    
    def handle_input(self, game_context, event):
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(game_context, event.key)
    
    def _handle_keydown(self, game_context, key):
        if key in (pygame.K_SPACE, pygame.K_UP):
            self._handle_jump(game_context)
        elif key == pygame.K_i:
            self._activate_invincibility(game_context)
    
    def _handle_jump(self, game_context):
        game_context.bird.bump()
        game_context.event_system.notify(JumpEvent())
    
    def _activate_invincibility(self, game_context):
        decorated = InvincibleBirdDecorator(game_context.bird, duration=3.0)
        game_context.bird = decorated
        game_context.sprite_manager.clear_group("bird")
        game_context.sprite_manager.add_to_group("bird", decorated)
    
    def update(self, game_context):
        self._update_sprites(game_context)
        self._update_managers(game_context)
        self._check_pipe_passing(game_context)
        self._update_difficulty(game_context)
        self._check_collisions(game_context)
    
    def _update_sprites(self, game_context):
        game_context.sprite_manager.update_group("bird")
        game_context.sprite_manager.update_group("ground")
        game_context.sprite_manager.update_group("pipes")
    
    def _update_managers(self, game_context):
        game_context.ground_manager.update_ground(game_context.resource_facade)
        game_context.pipe_manager.remove_offscreen_pipes(game_context.resource_facade)
    
    def _check_pipe_passing(self, game_context):
        bird_x = game_context.bird.rect[0]
        passed_count = game_context.pipe_manager.check_passed_pipes(bird_x)
        
        if passed_count > 0:
            game_context.event_system.notify(PipePassedEvent(2 * passed_count))
    
    def _update_difficulty(self, game_context):
        score = game_context.score_observer.get_score()
        new_factory = self._difficulty_manager.get_factory_for_score(
            score, game_context.pipe_manager._obstacle_factory
        )
        game_context.pipe_manager.update_factory(new_factory)
    
    def _check_collisions(self, game_context):
        bird = game_context.bird
        ground_group = game_context.sprite_manager.get_group("ground")
        pipe_group = game_context.sprite_manager.get_group("pipes")
        
        if self._collision_detector.detect_collision(bird, ground_group):
            self._handle_collision(game_context)
        elif self._collision_detector.detect_collision(bird, pipe_group):
            self._handle_collision(game_context)
    
    def _handle_collision(self, game_context):
        game_context.bird.die()
        game_context.event_system.notify(CollisionEvent())
        game_context.event_system.notify(GameOverEvent())
        time.sleep(1)
        game_context.game_over()
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.sprite_manager.draw_group("bird", screen)
        game_context.sprite_manager.draw_group("pipes", screen)
        game_context.sprite_manager.draw_group("ground", screen)
        self._render_score(game_context, screen)
    
    def _render_score(self, game_context, screen):
        score = game_context.score_observer.get_score()
        
        shadow = self._font.render(str(score), True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self._config.SCREEN_WIDTH // 2 + 3, 83))
        screen.blit(shadow, shadow_rect)
        
        text = self._font.render(str(score), True, (255, 255, 255))
        text_rect = text.get_rect(center=(self._config.SCREEN_WIDTH // 2, 80))
        screen.blit(text, text_rect)