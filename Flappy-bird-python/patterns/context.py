from entities.bird import Bird
from entities.ground import Ground
from entities.test_pipe import TestPipe
from patterns.ecs.auto_move import AutoMove
from patterns.ecs.box_collider import BoxCollider
from patterns.ecs.game_object import Component, GameObject
from patterns.ecs.sine_movement import SineMovement
from patterns.ecs.sprite_renderer import SpriteRenderer
from patterns.facade import *
from patterns.factory import *
from patterns.observer import *
from patterns.state.game_over_state import GameOverState
from patterns.state.menu_state import MenuState
from patterns.state.playing_state import PlayingState


class GameContext:
    """Contexto que gerencia o estado atual do jogo"""

    def __init__(self):
        # Sistema de eventos (Observer)
        self.game_objects: List[GameObject] = []

        self.event_system = GameEventSubject()
        self.score_observer = ScoreObserver()
        self.sound_observer = SoundObserver()
        self.event_system.attach(self.score_observer)
        self.event_system.attach(self.sound_observer)

        # Facade de recursos (carrega UMA vez)
        self.resource_facade = ResourceFacade()

        # Factory de obstáculos
        self.obstacle_factory = PipeFactory()

        # Recursos visuais
        self.background = self.resource_facade.get_scaled_background(
            SCREEN_WIDTH, SCREEN_HEIGHT
        )
        self.begin_image = self.resource_facade.get_image("message")

        # Grupos de sprites
        self.bird_group = pygame.sprite.Group()
        self.bird = Bird(self.resource_facade)
        self.bird_group.add(self.bird)

        self.ground_group = pygame.sprite.Group()
        for i in range(2):
            ground = Ground(GROUND_WIDTH * i, self.resource_facade)
            self.ground_group.add(ground)

        self.pipe_group = pygame.sprite.Group()
        for i in range(2):
            pipes = self.obstacle_factory.create_obstacle(
                SCREEN_WIDTH * i + 800, self.resource_facade
            )
            self.pipe_group.add(pipes[0])
            self.pipe_group.add(pipes[1])

            self.instantiate([TestPipe()], SCREEN_WIDTH + 800, SCREEN_HEIGHT - 200)
            self.instantiate([TestPipe(flipped=True)], SCREEN_WIDTH + 800, 0)

        # Estado inicial
        self._state = MenuState()

    def instantiate(self, components: List[Component], x: int, y: int, name=None):
        go = GameObject(context=self, x=x, y=y, name=name)

        for c in components:
            c.game_object = go
            go.add_component(c)

        self.game_objects.append(go)
        return go

    def _set_state(self, state):
        """Muda o estado do jogo"""
        self._state = state

    def handle_input(self, event):
        """Delega input para o estado atual"""
        self._state.handle_input(self, event)

    def update(self):
        """Atualiza o estado atual"""
        dt = 1

        self._state.update(self)

        for go in self.game_objects:
            go.update(dt)

    def render(self, screen):
        """Renderiza o estado atual"""
        self._state.render(self, screen)
        for go in self.game_objects:
            sprite = go.get_component(SpriteRenderer)
            if sprite and isinstance(sprite, SpriteRenderer):
                sprite.render(screen)

    def find_object(self, name) -> GameObject | None:
        for go in self.game_objects:
            if go.name == name:
                return go

        return None

    def play(self):
        self._set_state(PlayingState())

    def game_over(self):
        self._set_state(GameOverState())

    def set_menu(self):
        self._set_state(MenuState())

    def get_colliders(self) -> List[BoxCollider]:
        colliders = []

        for go in self.game_objects:
            collider = go.get_component(BoxCollider)
            if collider is not None:
                colliders.append(collider)

        return colliders

    def reset_game(self):
        """Reinicia o jogo"""
        # Reseta pontuação
        self.event_system.notify(ResetEvent())

        # Reseta factory para pipes normais
        self.obstacle_factory = PipeFactory()

        # Reseta pássaro
        self.bird_group.empty()
        self.bird = Bird(self.resource_facade)
        self.bird_group.add(self.bird)

        # Reseta pipes
        self.pipe_group.empty()
        for i in range(2):
            pipes = self.obstacle_factory.create_obstacle(
                SCREEN_WIDTH * i + 800, self.resource_facade
            )
            self.pipe_group.add(pipes[0])
            self.pipe_group.add(pipes[1])
