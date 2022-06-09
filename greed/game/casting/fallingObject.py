from game.casting.actor import Actor
from game.shared.point import Point


class FallingObject(Actor):
    """
    Authors: Alvaro and Camden
    A constantly falling object

    """
    def __init__(self):
        super().__init__()
        self._velocity = Point(0,1)
        
    def fall(self):
        self.add(1)
