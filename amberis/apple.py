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

import random

import pygame

from settings import GameSettings


class Apple:

    def __init__(self):
        self.x = random.randint(
            0, GameSettings.CELL_WIDTH - 1) * GameSettings.CELL_SIZE
        self.y = random.randint(
            0, GameSettings.CELL_HEIGHT - 1) * GameSettings.CELL_SIZE

        self.rect = pygame.rect.Rect((self.x, self.y,
                                      GameSettings.CELL_SIZE,
                                      GameSettings.CELL_SIZE))
        self.value = random.randint(0, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, GameSettings.RED, self.rect)
