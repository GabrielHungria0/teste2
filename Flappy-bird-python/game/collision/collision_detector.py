"""Sistema de detecção de colisões baseado em can_collide()."""
import pygame


class CollisionDetector:

    def detect_collision(self, bird, obstacle_group):
        if not bird.can_collide():
            return False
        
        return pygame.sprite.spritecollide(
            bird, obstacle_group, False, pygame.sprite.collide_mask
        )