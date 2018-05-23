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

from block import Block
from snake import Snake
from settings import GameSettings


class Game:

    def set_screen(self):
        screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE)
        pygame.display.set_caption("Snake matemático")
        screen.fill(GameSettings.BACKGROUND)

        pygame.display.flip()
        return screen

    def centralized_text(self, text, screen):
        # Centralizes text. Takes the screen width divides by two, then
        # gets the width of the text and divides by two, after subtract
        # one by another.
        screen.blit(text, ((
            GameSettings.SCREEN_SIZE[0] / 2)
            - (text.get_rect().width / 2),
            (GameSettings.SCREEN_SIZE[1] / 2) - 50))

    def show_title(self, screen):
        title_font = pygame.font.SysFont("hack", 100)
        title = title_font.render("Amberis", 1, (255, 255, 255))
        self.centralized_text(title, screen)

    def run(self):
        pygame.init()
        snake = Snake()
        done = False
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("hack", 50)

        while snake.is_alive() or done is False:
            clock.tick(60)

            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen = self.set_screen()
            snake.draw(screen)
            snake.handle_keys()

            if (snake.on_border()):
                label = font.render("Você morreu", 1, (255, 255, 255))
                self.centralized_text(label, screen)
                snake.alive = False
                done = True
                break

            block = Block()
            block.draw(screen)

            pygame.display.update()

        pygame.quit()
