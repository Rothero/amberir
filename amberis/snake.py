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

import pygame

from settings import GameSettings


class Snake:

    def __init__(self):
        self.length = 1
        self.rect = pygame.rect.Rect((
            GameSettings.SCREEN_SIZE[0] / 2,
            GameSettings.SCREEN_SIZE[1] / 2, 50, 50))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        distance = 15

        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, distance)
        elif key[pygame.K_UP]:
            self.rect.move_ip(0, -distance)

        if key[pygame.K_RIGHT]:
            self.rect.move_ip(distance, 0)
        elif key[pygame.K_LEFT]:
            self.rect.move_ip(-distance, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, GameSettings.WHITE, self.rect)
        self.rect.clamp_ip(screen.get_rect())
