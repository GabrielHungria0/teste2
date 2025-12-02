"""Serviço para orquestrar lógica central do jogo durante o estado Playing."""
from patterns.chain_of_responsibility.difficulty_manager import DifficultyManager
from patterns.event import PipePassedEvent


class GameplayService:
    """Orquestra lógica de jogo: atualizações de sprites, managers e dificuldade."""
    
    def __init__(self):
        self._difficulty_manager = DifficultyManager()
    
    def update(self, game_context):
        """Executa todas as atualizações de jogo em ordem."""
        self._update_sprites(game_context)
        self._update_managers(game_context)
        self._check_pipe_passing(game_context)
        self._update_difficulty(game_context)
        game_context.collision_manager.check_and_handle(game_context)
    
    def _update_sprites(self, game_context):
        """Atualiza animações e posições de sprites."""
        game_context.sprite_manager.update_group("bird")
        game_context.sprite_manager.update_group("ground")
        game_context.sprite_manager.update_group("pipes")
    
    def _update_managers(self, game_context):
        """Atualiza estado de managers (chão, pipes)."""
        game_context.ground_manager.update_ground(game_context.resource_facade)
        game_context.pipe_manager.remove_offscreen_pipes(game_context.resource_facade)
    
    def _check_pipe_passing(self, game_context):
        """Verifica se o pássaro passou por um pipe e notifica pontuação."""
        bird_x = game_context.bird.rect[0]
        passed_count = game_context.pipe_manager.check_passed_pipes(bird_x)
        
        if passed_count > 0:
            game_context.event_system.notify(PipePassedEvent(2 * passed_count))
    
    def _update_difficulty(self, game_context):
        """Ajusta dificuldade (factory de pipes) baseado na pontuação."""
        score = game_context.score_observer.get_score()
        current_factory = game_context.pipe_manager.get_obstacle_factory()
        new_factory = self._difficulty_manager.get_factory_for_score(score, current_factory)
        game_context.pipe_manager.update_factory(new_factory)
