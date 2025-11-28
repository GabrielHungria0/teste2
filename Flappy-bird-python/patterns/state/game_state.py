from abc import ABC, abstractmethod


class GameState(ABC):

    @abstractmethod
    def handle_input(self, game_context, event):
        pass

    @abstractmethod
    def update(self, game_context):
        pass

    @abstractmethod
    def render(self, game_context, screen):
        pass
