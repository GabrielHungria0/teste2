from pygame import K_RETURN, K_SPACE, KEYDOWN
from patterns.state import GameState
from game.managers.hud_renderer import HUDRenderer


class GameOverState(GameState):
    def __init__(self):
        self._hud_renderer = HUDRenderer()
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN and self._is_restart_key(event.key):
            game_context.entity_facade.reset_game()
            game_context.state_manager.transition_to_menu()
    
    def _is_restart_key(self, key):
        return key in (K_SPACE, K_RETURN)
    
    def update(self, game_context):
        pass
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.sprite_manager.draw_group("bird", screen)
        game_context.sprite_manager.draw_group("pipes", screen)
        game_context.sprite_manager.draw_group("ground", screen)
        
        self._hud_renderer.render_game_over(screen)
        score = game_context.score_observer.get_score()
        self._hud_renderer.render_final_score(screen, score)
        self._hud_renderer.render_restart_instructions(screen)