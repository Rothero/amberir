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

import sys

import pygame

from settings import GameSettings


class Snake:

    def __init__(self):
        self.length = 2
        # Starts in the center of the screen.
        self.coords = [
            {
                "x": (GameSettings.SCREEN_WIDTH / 2) - GameSettings.CELL_SIZE,
                "y": (GameSettings.SCREEN_HEIGHT / 2) - GameSettings.CELL_SIZE
            },
            {
                "x": (GameSettings.SCREEN_WIDTH / 2) - GameSettings.CELL_SIZE,
                "y": (GameSettings.SCREEN_HEIGHT
                      / 2) - GameSettings.CELL_SIZE * 2
            }
        ]
        self.alive = True
        self.direction = 'up'

    def handle_keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.direction = 'down'
        elif key[pygame.K_UP]:
            self.direction = 'up'
        elif key[pygame.K_RIGHT]:
            self.direction = 'right'
        elif key[pygame.K_LEFT]:
            self.direction = 'left'

        # Quits game.
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def set_direction(self):
        if self.direction == "down":
            new_position = {"x": self.coords[0]["x"],
                            "y": self.coords[0]["y"] + GameSettings.CELL_SIZE}
        elif self.direction == "up":
            new_position = {"x": self.coords[0]["x"],
                            "y": self.coords[0]["y"] - GameSettings.CELL_SIZE}
        elif self.direction == "right":
            new_position = {"x": self.coords[0]["x"] + GameSettings.CELL_SIZE,
                            "y": self.coords[0]["y"]}
        elif self.direction == "left":
            new_position = {"x": self.coords[0]["x"] - GameSettings.CELL_SIZE,
                            "y": self.coords[0]["y"]}

        self.coords.insert(0, new_position)
        del self.coords[-1]

    def hit_itself(self):
        # Checks if the snake hit itself.
        for coord in self.coords[1:]:
            if (coord["x"] == self.coords[0]["x"] and
                    coord["y"] == self.coords[0]["y"]):
                return True

        return False

    def ate_apple(self, apple):
        if (self.coords[0]["x"] == apple.rect[0] and
                self.coords[0]["y"] == apple.rect[1]):
            return True

        return False

    def is_alive(self):
        """Checks if the snake is still alive. """
        return self.alive

    def on_border(self):
        """Checks if the snake in on the border. """
        if (self.coords[1]["x"] == -GameSettings.CELL_SIZE or
            self.coords[1]["y"] == -GameSettings.CELL_SIZE or
            self.coords[1]["x"] >= GameSettings.SCREEN_WIDTH or
                self.coords[1]["y"] >= GameSettings.SCREEN_HEIGHT):
            return True

        return False

    def draw(self, screen):
        for coord in self.coords:
            rect = pygame.rect.Rect((coord["x"], coord["y"],
                                     GameSettings.CELL_SIZE,
                                     GameSettings.CELL_SIZE))
            rect_border = pygame.rect.Rect((coord["x"], coord["y"],
                                            GameSettings.CELL_SIZE / 2,
                                            GameSettings.CELL_SIZE / 2))
            pygame.draw.rect(screen, GameSettings.WHITE, rect)
            pygame.draw.rect(screen, GameSettings.LIGHT_GRAY, rect_border)
