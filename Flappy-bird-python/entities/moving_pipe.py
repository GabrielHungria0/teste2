from entities.pipe import Pipe


class MovingPipe(Pipe):
    def __init__(self, inverted, xpos, ysize, resource_facade, 
                 movement_range=50, movement_speed=2):
        super().__init__(inverted, xpos, ysize, resource_facade)
        
        self._movement_range = movement_range
        self._movement_speed = movement_speed
        self._movement_offset = 0
        self._movement_direction = 1
        self._initial_y = self.rect[1]
    
    def update(self):
        """Atualiza posição horizontal e vertical do pipe."""
        self._move_horizontal()
        self._move_vertical()
    
    def _move_vertical(self):
        self._update_movement_offset()
        self._apply_vertical_position()
    
    def _update_movement_offset(self):
        self._movement_offset += self._movement_speed * self._movement_direction
        
        if abs(self._movement_offset) >= self._movement_range:
            self._movement_direction *= -1
    
    def _apply_vertical_position(self):
        self.rect[1] = int(self._initial_y + self._movement_offset)