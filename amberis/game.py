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

from apple import Apple
from snake import Snake
from settings import GameSettings


class Game:

    def __init__(self):
        self.score = 0
        self.screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE)

    def set_screen(self):
        pygame.display.set_caption("Snake matemático")
        self.screen.fill(GameSettings.BACKGROUND)

    def draw_background_chain(self):
        for line in range(0,
                          GameSettings.SCREEN_SIZE[0],
                          GameSettings.CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GameSettings.GREEN, (line, 0),
                (line, GameSettings.SCREEN_SIZE[1]))

        for column in range(0,
                            GameSettings.SCREEN_SIZE[1],
                            GameSettings.CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GameSettings.GREEN, (0, column),
                (GameSettings.SCREEN_SIZE[0], column))

    def centralized_text(self, text):
        """
        Centralizes text. Takes the screen width divides by two, then
        gets the width of the text and divides by two, after subtract
        one by another.
        """
        text_width = text.get_rect().width
        self.screen.blit(text, ((
            GameSettings.SCREEN_SIZE[0] / 2) - (text_width / 2),
            (GameSettings.SCREEN_SIZE[1] / 2) - 50))

    def show_title(self):
        title_font = pygame.font.SysFont("hack", 100)
        title = title_font.render("Amberis", 1, GameSettings.WHITE)
        self.centralized_text(title)

    def draw_score(self):
        score_text = pygame.font.SysFont("hack", 15)
        score = score_text.render(
            "Score: " + str(self.score), 1, GameSettings.BLUE)
        self.screen.blit(score, (50, 50))

    def run(self):
        pygame.init()
        snake = Snake()
        done = False
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("hack", 50)
        apple = Apple()
        self.set_screen()
        self.draw_background_chain()

        while done is False:
            clock.tick(10)

            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.draw_score()
            snake.draw(self.screen)
            snake.handle_keys()
            snake.set_direction()

            apple.draw(self.screen)

            if (snake.on_border()):
                label = font.render("Você morreu", 1, GameSettings.BLUE)
                self.centralized_text(label)
                snake.alive = False
                done = True

            if (apple.rect[0] - snake.rect[0] == snake.rect[0] and
                    apple.rect[1] - snake.rect[1] == snake.rect[1]):
                print("asda")

            pygame.display.update()

        pygame.quit()
