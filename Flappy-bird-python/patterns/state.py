
from abc import ABC, abstractmethod
from enum import Enum
import pygame
from pygame.locals import *
import time
from entities.ground import Ground
from utils.helpers import is_off_screen
from config import SCREEN_WIDHT, GROUND_WIDHT, PIPE_WIDHT
from patterns.factory import (PipeFactory, MovingPipeFactory, 
                                      NarrowPipeFactory, AlternatingMovingPipeFactory)
from patterns.decorator import InvincibleBirdDecorator


class GameStateEnum(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3


class GameState(ABC):
    
    @abstractmethod
    def handle_input(self, game_context, event):
        pass
    
    @abstractmethod
    def update(self, game_context):
        pass
    
    @abstractmethod
    def render(self, game_context, screen):
        pass


class MenuState(GameState):
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                game_context.event_system.notify("JUMP")
                game_context.set_state(PlayingState())
    
    def update(self, game_context):
        game_context.bird.begin()
        game_context.ground_group.update()
        
        if is_off_screen(game_context.ground_group.sprites()[0]):
            game_context.ground_group.remove(game_context.ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDHT - 20, game_context.resource_facade)
            game_context.ground_group.add(new_ground)
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        screen.blit(game_context.begin_image, (120, 150))
        game_context.bird_group.draw(screen)
        game_context.ground_group.draw(screen)


class PlayingState(GameState):
    
    def __init__(self):
        self.pipe_pairs_passed = set()
        self.last_difficulty = 0
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                game_context.bird.bump()
                game_context.event_system.notify("JUMP")
            # Ativa invencibilidade temporária ao pressionar I (exemplo de uso do decorator)
            if event.key == K_i:
                # Substitui o bird por uma instância decorada
                decorated = InvincibleBirdDecorator(game_context.bird, duration=3.0)
                # atualiza referências no contexto
                game_context.bird = decorated
                # trocar a merda do passaro
                game_context.bird_group.empty()
                game_context.bird_group.add(decorated)
    
    def update(self, game_context):
        game_context.bird_group.update()
        game_context.ground_group.update()
        game_context.pipe_group.update()
        
        # Gerencia ground (usa o ground mais à esquerda)
        if game_context.ground_group.sprites():
            left_ground = min(game_context.ground_group.sprites(), key=lambda g: g.rect[0])
            if is_off_screen(left_ground):
                game_context.ground_group.remove(left_ground)
                new_ground = Ground(GROUND_WIDHT - 20, game_context.resource_facade)
                game_context.ground_group.add(new_ground)
        
        # Gerencia pipes (remove o par cujo pipe mais à esquerda saiu da tela)
        if game_context.pipe_group.sprites():
            left_pipe = min(game_context.pipe_group.sprites(), key=lambda p: p.rect[0])
            if is_off_screen(left_pipe):
                pid = getattr(left_pipe, 'pair_id', None)
                if pid is not None:
                    # remove todos os pipes com esse pair_id
                    to_remove = [p for p in game_context.pipe_group.sprites() if getattr(p, 'pair_id', None) == pid]
                    for p in to_remove:
                        game_context.pipe_group.remove(p)
                else:
                    # fallback: remove o pipe mais à esquerda e a próxima entrada
                    game_context.pipe_group.remove(left_pipe)
                    # tenta remover outro pipe que esteja logo após (se existir)
                    sprites = game_context.pipe_group.sprites()
                    if sprites:
                        second = min(sprites, key=lambda p: p.rect[0])
                        game_context.pipe_group.remove(second)

                pipes = game_context.obstacle_factory.create_obstacle(SCREEN_WIDHT * 2, game_context.resource_facade)
                game_context.pipe_group.add(pipes[0])
                game_context.pipe_group.add(pipes[1])
        
        pipes_list = game_context.pipe_group.sprites()
        seen_pairs = {}
        for p in pipes_list:
            pid = getattr(p, 'pair_id', None)
            if pid is not None:
                # guarda a primeira ocorrência do pipe (usada para pegar coordenada x)
                if pid not in seen_pairs:
                    seen_pairs[pid] = p

        bird_x = game_context.bird.rect[0]
        for pid, pipe_example in seen_pairs.items():
            # verifica se já contámos esse par
            if pid in self.pipe_pairs_passed:
                continue

            pipe_x = pipe_example.rect[0]
            # quando o pássaro passou da borda direita do cano, conta 1 ponto
            if bird_x > pipe_x + PIPE_WIDHT:
                # DEBUG: imprime informações para diagnóstico
                try:
                    current_score = game_context.score_observer.get_score()
                except Exception:
                    current_score = 'unknown'
                self.pipe_pairs_passed.add(pid)
                game_context.event_system.notify("PIPE_PASSED")
        
        # Sistema de progressão de dificuldade
        self._update_difficulty(game_context)
        
        # Detecta colisões — suporta decoradores que expõem `check_collision(group)`
        collision = False
        for bird in game_context.bird_group.sprites():
            # Se o sprite estiver decorado e expuser check_collision, use-o
            if hasattr(bird, 'check_collision'):
                if bird.check_collision(game_context.ground_group) or bird.check_collision(game_context.pipe_group):
                    collision = True
                    break
            else:
                # fallback: usa as checagens padrão do pygame
                if pygame.sprite.spritecollide(bird, game_context.ground_group, False, pygame.sprite.collide_mask):
                    collision = True
                    break
                if pygame.sprite.spritecollide(bird, game_context.pipe_group, False, pygame.sprite.collide_mask):
                    collision = True
                    break

        if collision:
            game_context.event_system.notify("COLLISION")
            game_context.event_system.notify("GAME_OVER")
            time.sleep(1)
            game_context.set_state(GameOverState())
    
    def _update_difficulty(self, game_context):
        """Atualiza dificuldade baseada na pontuação"""
        
        score = game_context.score_observer.get_score()
        
        # Evita mudanças repetidas
        if score == self.last_difficulty:
            return
        
        # Nível 1: Pipes normais (0-3 pontos)
        if score < 3 and not isinstance(game_context.obstacle_factory, PipeFactory):
            game_context.obstacle_factory = PipeFactory()
            self.last_difficulty = score
        
        # Nível 2: Pipes que se movem (3-6 pontos)
        elif 3 <= score < 6 and not isinstance(game_context.obstacle_factory, MovingPipeFactory):
            game_context.obstacle_factory = MovingPipeFactory()
            self.last_difficulty = score
        
        # Nível 3: Pipes estreitos (6-10 pontos)
        elif 6 <= score < 10 and not isinstance(game_context.obstacle_factory, NarrowPipeFactory):
            game_context.obstacle_factory = NarrowPipeFactory()
            self.last_difficulty = score
        
        # Nível 4: Pipes alternados! (10+ pontos)
        elif score >= 10 and not isinstance(game_context.obstacle_factory, AlternatingMovingPipeFactory):
            game_context.obstacle_factory = AlternatingMovingPipeFactory()
            self.last_difficulty = score
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.bird_group.draw(screen)
        game_context.pipe_group.draw(screen)
        game_context.ground_group.draw(screen)
        
        self._render_score(game_context, screen)
    
    def _render_score(self, game_context, screen):
        """Renderiza a pontuação na tela"""
        font = pygame.font.Font(None, 72)
        score = game_context.score_observer.get_score()
        text = font.render(str(score), True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDHT // 2, 80))
        
        shadow = font.render(str(score), True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(SCREEN_WIDHT // 2 + 3, 83))
        
        screen.blit(shadow, shadow_rect)
        screen.blit(text, text_rect)


class GameOverState(GameState):
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_RETURN:
                game_context.reset_game()
                game_context.set_state(MenuState())
    
    def update(self, game_context):
        pass
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.bird_group.draw(screen)
        game_context.pipe_group.draw(screen)
        game_context.ground_group.draw(screen)
        
        # Texto de Game Over
        font = pygame.font.Font(None, 74)
        text = font.render('GAME OVER', True, (255, 0, 0))
        screen.blit(text, (50, 200))
        
        # Pontuação final
        score = game_context.score_observer.get_score()
        font_score = pygame.font.Font(None, 48)
        text_score = font_score.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text_score, (120, 280))
        
        # Instruções
        font_small = pygame.font.Font(None, 36)
        text_restart = font_small.render('Press SPACE to restart', True, (255, 255, 255))
        screen.blit(text_restart, (60, 350))