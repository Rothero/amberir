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


class Block:

    def __init__(self):
        self.rect = pygame.rect.Rect((
            random.randint(0, GameSettings.SCREEN_SIZE[0]),
            random.randint(0, GameSettings.SCREEN_SIZE[1]), 50, 50))
        self.value = 1

    def exits(self):
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, GameSettings.RED, self.rect)
        self.rect.clamp_ip(screen.get_rect())
