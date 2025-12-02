from pygame import K_SPACE, K_UP, KEYDOWN, Surface
from patterns.event import JumpEvent
from patterns.state.game_state import GameState


class InitialScreenState(GameState):
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN and self._is_start_key(event.key):
            game_context.event_system.notify(JumpEvent())
            game_context.state_facade.play()
    
    def _is_start_key(self, key):
        return key in (K_SPACE, K_UP)
    
    def update(self, game_context):
        game_context.bird.begin()
        game_context.sprite_manager.update_group("ground")
        game_context.ground_manager.update_ground(game_context.resource_facade)
    
    def render(self, game_context, screen: Surface):
        screen.blit(game_context.background, (0, 0))
        screen.blit(game_context.begin_image, (120, 150))
        game_context.sprite_manager.draw_group("bird", screen)
        game_context.sprite_manager.draw_group("ground", screen)