from typing import List, Type, override

from abc import ABC, abstractmethod
from typing import List, Type, TypeVar, Optional
import uuid


class Component(ABC):
    def __init__(self):
        self.game_object: GameObject = NullGameObject()

    def destroy(self):
        self.game_object.destroy()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def dispose(self):
        pass


T = TypeVar("T", bound=Component)


class GameObject:
    def __init__(self, context, name=None, x=0, y=0):
        self.context = context
        self.name = f"GameObject{uuid.uuid4().hex}"

        if name is not None:
            self.name = name

        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.components: List[Component] = []
        self.is_active = True

    def add_component(self, component: Component):
        self.components.append(component)
        component.start()
        component.game_object = self
        return component

    def get_component(self, component_type: Type[T]) -> Optional[T]:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def update(self, dt):
        if not self.is_active:
            return
        for component in self.components:
            component.update(dt)

    def destroy(self):
        for c in self.components:
            c.dispose()

        self.context.game_objects.remove(self)

    def find_object(self, name):
        return self.context.find_object(name)


class NullGameObject(GameObject):
    def __init__(self, name=f"GameObject{uuid.uuid4().hex}", x=0, y=0):
        self.components = []
        pass

    @override
    def add_component(self, component: Component) -> Component:
        return super().add_component(component)

    def get_component(self, component_type: Type):
        pass

    def update(self, dt):
        pass
