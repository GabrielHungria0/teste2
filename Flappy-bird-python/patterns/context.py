import pygame
from config import GameConfig
from patterns.event import ResetEvent
from patterns.facade import ResourceFacade
from patterns.factory import PipeFactory
from game.managers import PipeManager, GroundManager
from patterns.observer import GameEventSubject, ScoreObserver, SoundObserver
from game.managers.sprite_manager import SpriteManager
from patterns.state.game_state_manager import GameStateManager
from patterns.initializers import GameInitializer


class GameContext:
    def __init__(self):
        self._config = GameConfig()
        self._initializer = GameInitializer()
        self._initialize_systems()
        self._initialize_resources()
        self._initialize_entities()
        self._state_manager = GameStateManager()

    def _initialize_systems(self):
        self.event_system = GameEventSubject()
        self.score_observer = ScoreObserver()
        self.sprite_manager = SpriteManager()
        self.sprite_manager.create_group("bird")
        self.sprite_manager.create_group("ground")
        self.sprite_manager.create_group("pipes")

    def _initialize_resources(self):
        self.resource_facade = ResourceFacade()
        self.sound_observer = SoundObserver(self.resource_facade)
        self.event_system.attach(self.score_observer)
        self.event_system.attach(self.sound_observer)
        bg_image = self.resource_facade.get_image("background")
        self.background = pygame.transform.scale(
            bg_image,
            (self._config.SCREEN_WIDTH, self._config.SCREEN_HEIGHT)
        )
        self.begin_image = self.resource_facade.get_image("message")

    def _initialize_entities(self):
        self.bird = self._initializer.initialize_bird(self.sprite_manager, self.resource_facade)
        self.ground_manager = GroundManager(self.sprite_manager)
        self._initializer.initialize_ground(self.sprite_manager, self.resource_facade)
        self.pipe_manager = self._initializer.initialize_pipes(self.sprite_manager, self.resource_facade)

    def handle_input(self, event):
        self._state_manager.handle_input(self, event)

    def update(self):
        self._state_manager.update(self)

    def render(self, screen):
        self._state_manager.render(self, screen)

    def play(self):
        self._state_manager.transition_to_playing()

    def game_over(self):
        self._state_manager.transition_to_game_over()

    def set_menu(self):
        self._state_manager.transition_to_menu()

    def reset_game(self):
        self.event_system.notify(ResetEvent())
        self._reset_bird()
        self._reset_pipes()

    def _reset_bird(self):
        self.sprite_manager.clear_group("bird")
        self.bird = self._initializer.initialize_bird(self.sprite_manager, self.resource_facade)

    def _reset_pipes(self):
        self.sprite_manager.clear_group("pipes")
        self.pipe_manager = self._initializer.initialize_pipes(self.sprite_manager, self.resource_facade)