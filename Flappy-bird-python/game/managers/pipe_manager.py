from config import GameConfig
from utils.helpers import is_sprite_off_screen


class PipeManager:
    """Gerencia criação, remoção e pontuação de pares de pipes."""
    def __init__(self, sprite_manager, obstacle_factory):
        self._config = GameConfig()
        self._sprite_manager = sprite_manager
        self._obstacle_factory = obstacle_factory
        self._passed_pairs = set()
    
    def update_factory(self, new_factory):
        """Atualiza a factory de obstáculos."""
        self._obstacle_factory = new_factory
    
    def get_obstacle_factory(self):
        """Retorna a factory atual (encapsulamento)."""
        return self._obstacle_factory
    
    def add_pair(self, xpos, resource_facade):
        """Adiciona um novo par de pipes à tela."""
        pipes = self._obstacle_factory.create_obstacle(xpos, resource_facade)
        for pipe in pipes:
            self._sprite_manager.add_to_group("pipes", pipe)
    
    def remove_offscreen_pipes(self, resource_facade):
        """Remove pipes que saíram da tela e adiciona novos."""
        pipes = self._sprite_manager.get_sprites("pipes")
        if not pipes:
            return
        
        left_pipe = min(pipes, key=lambda p: p.rect[0])
        
        if is_sprite_off_screen(left_pipe):
            self._remove_pipe_pair(left_pipe)
            self.add_pair(self._config.SCREEN_WIDTH * 2, resource_facade)
    
    def _remove_pipe_pair(self, pipe):
        """Remove um par completo de pipes pelo pair_id."""
        pair_id = getattr(pipe, "pair_id", None)
        pipes = self._sprite_manager.get_sprites("pipes")
        
        if pair_id:
            to_remove = [p for p in pipes if getattr(p, "pair_id", None) == pair_id]
            for p in to_remove:
                self._sprite_manager.remove_from_group("pipes", p)
        else:
            self._sprite_manager.remove_from_group("pipes", pipe)
    
    def check_passed_pipes(self, bird_x):
        """Verifica quantos pares novos o pássaro passou."""
        pipes = self._sprite_manager.get_sprites("pipes")
        seen_pairs = self._get_unique_pairs(pipes)
        
        newly_passed = []
        for pair_id, pipe in seen_pairs.items():
            if pair_id not in self._passed_pairs:
                if self._bird_passed_pipe(bird_x, pipe):
                    self._passed_pairs.add(pair_id)
                    newly_passed.append(pair_id)
        
        return len(newly_passed)
    
    def _get_unique_pairs(self, pipes):
        """Obtém um dicionário de pares únicos de pipes."""
        seen = {}
        for pipe in pipes:
            pair_id = getattr(pipe, "pair_id", None)
            if pair_id and pair_id not in seen:
                seen[pair_id] = pipe
        return seen
    
    def _bird_passed_pipe(self, bird_x, pipe):
        """Verifica se o pássaro já passou completamente de um pipe."""
        return bird_x > pipe.rect[0] + self._config.PIPE_WIDTH
    
    def reset(self):
        """Reseta o rastreamento de pares passados."""
        self._passed_pairs.clear()