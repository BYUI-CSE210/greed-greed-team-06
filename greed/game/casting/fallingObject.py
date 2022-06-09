from game.casting.actor import Actor
from game.shared.point import Point


class FallingObject(Actor):
    """
    Authors: Alvaro and Camden
    A constantly falling object
        Attributes:
              _velocity: the speed and direction of the object.
    """
    def __init__(self):
        super().__init__()
        self._velocity = Point(0,1)
        
        
