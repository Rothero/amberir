"""
Edison Neto, Roger Rojas, Kalvin Vasconcelos, Kaique Juvêncio
This software simply converts a number in some numerical base to decimal

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
        self.length = 1
        self.x = (GameSettings.SCREEN_SIZE[0] / 2) - GameSettings.CELL_SIZE
        self.y = (GameSettings.SCREEN_SIZE[1] / 2) - GameSettings.CELL_SIZE
        self.rect = pygame.rect.Rect((self.x, self.y,
                                      GameSettings.CELL_SIZE,
                                      GameSettings.CELL_SIZE))
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
            self.x = self.rect[0]
            self.y = self.rect[1] + GameSettings.CELL_SIZE
            self.rect = pygame.rect.Rect((self.x, self.y,
                                          GameSettings.CELL_SIZE,
                                          GameSettings.CELL_SIZE))
            # self.rect.move_ip(0, GameSettings.CELL_SIZE)
        elif self.direction == "up":
            self.x = self.rect[0]
            self.y = self.rect[1] - GameSettings.CELL_SIZE
            self.rect = pygame.rect.Rect((self.x, self.y,
                                          GameSettings.CELL_SIZE,
                                          GameSettings.CELL_SIZE))
            # self.rect.move_ip(0, -GameSettings.CELL_SIZE)
        elif self.direction == "right":
            self.x = self.rect[0] + GameSettings.CELL_SIZE
            self.y = self.rect[1]
            self.rect = pygame.rect.Rect((self.x, self.y,
                                          GameSettings.CELL_SIZE,
                                          GameSettings.CELL_SIZE))
            # self.rect.move_ip(GameSettings.CELL_SIZE, 0)
        elif self.direction == "left":
            self.x = self.rect[0] - GameSettings.CELL_SIZE
            self.y = self.rect[1]
            self.rect = pygame.rect.Rect((self.x, self.y,
                                          GameSettings.CELL_SIZE,
                                          GameSettings.CELL_SIZE))
            # self.rect.move_ip(-GameSettings.CELL_SIZE, 0)

    def is_alive(self):
        """Checks if the snake is still alive. """
        return self.alive

    def on_border(self):
        """Checks if the snake in on the border. """
        if (self.rect[0] == -GameSettings.CELL_SIZE or
            self.rect[1] == -GameSettings.CELL_SIZE or
            self.rect[0] >= GameSettings.SCREEN_SIZE[0] or
                self.rect[1] >= GameSettings.SCREEN_SIZE[1]):
            return True

        return False

    def draw(self, screen):
        pygame.draw.rect(screen, GameSettings.WHITE, self.rect)
        self.rect.clamp_ip(screen.get_rect())
