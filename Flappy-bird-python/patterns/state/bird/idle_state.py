# patterns/state/bird/idle_state.py

from .bird_state_interface import BirdState
# NUNCA importe FlyingState no topo!

class IdleState(BirdState):
    def update(self, bird):
        bird._update_sprite()
    
    def bump(self, bird):
        # SOLUÇÃO PARA O CICLO DE IMPORTAÇÃO: Importação LOCAL
        # A instância FlyingState só é criada aqui, após a inicialização do programa.
        from .flying_state import FlyingState 
        
        bird.set_state(FlyingState())
        # O acesso a _speed e _config em Bird (Contexto) é parte do padrão.
        bird._speed = -bird._config.SPEED
    
    def can_collide(self):
        return False