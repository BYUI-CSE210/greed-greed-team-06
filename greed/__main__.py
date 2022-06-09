import os
import random

from game.casting.actor import Actor
from game.casting.fallingObject import FallingObject
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.fallingObject import FallingObject


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ROCKS = 20
DEFAULT_GEMS = 20


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("The Score")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - 20)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
    # create the falling gem

    for n in range(DEFAULT_GEMS):
        x = random.randint(0, COLS-1)
        y = random.randint(1, ROWS-1)
        position = Point(x,y)
        position = position.scale(CELL_SIZE)

        r= random.randint(0,225)
        g= random.randint(0,225)
        b= random.randint(0,225)
        color = Color(r,g,b)

        gem = FallingObject()
        gem.set_text("*")
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        cast.add_actor("gems", gem)

#add falling rock
    for n in range(DEFAULT_ROCKS):
        x = random.randint(0, COLS-1)
        y = random.randint(1, ROWS-1)
        position = Point(x,y)
        position = position.scale(CELL_SIZE)

        r= random.randint(0,225)
        g= random.randint(0,225)
        b= random.randint(0,225)
        color = Color(r,g,b)

        rock = FallingObject()
        rock.set_text("O")
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        cast.add_actor("rocks", rock)


    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()