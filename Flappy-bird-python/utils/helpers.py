def is_sprite_off_screen(sprite):
   
    return sprite.rect[0] < -(sprite.rect[2])