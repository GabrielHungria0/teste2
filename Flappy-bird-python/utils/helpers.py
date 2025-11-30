def is_sprite_off_screen(sprite):
    """Verifica se um sprite passou completamente para a esquerda da tela.
    
    Args:
        sprite: Sprite pygame com rect attribute
        
    Returns:
        bool: True se o sprite está fora de tela à esquerda
    """
    return sprite.rect[0] < -(sprite.rect[2])