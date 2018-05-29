"""
Edison Neto, Roger Rojas, Kalvin Vasconcelos, Kaique Juvêncio
It's a simple clone of the classic snake game.

Copyright (C) 2018 Edison Neto
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


class GameSettings:
    BACKGROUND = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (0, 0, 127)
    LIGHT_GRAY = (192, 192, 192)
    LIGHT_GREEN = (182, 234, 32)

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

    CELL_SIZE = 50
    CELL_WIDTH = int(SCREEN_WIDTH / CELL_SIZE)
    CELL_HEIGHT = int(SCREEN_HEIGHT / CELL_SIZE)
