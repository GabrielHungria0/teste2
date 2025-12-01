# patterns/state/__init__.py

from .game_state import GameState
from .menu_state import MenuState
from .playing_state import PlayingState
from .game_over_state import GameOverState

# --- CORREÇÃO E RE-EXPORTAÇÃO ---
from .bird.bird_state_interface import BirdState # Mudei para bird_state_interface
from .bird.idle_state import IdleState
from .bird.flying_state import FlyingState
from .bird.dead_state import DeadState
# --------------------------------