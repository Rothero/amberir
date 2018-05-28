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

from apple import Apple
from snake import Snake
from settings import GameSettings


class Game:

    def __init__(self):
        self.score = "0"
        self.screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE)

    def set_caption(self):
        pygame.display.set_caption("Snake matemático")

    def set_screen(self):
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

        click_font = pygame.font.SysFont("hack", 20)
        click_text = click_font.render(
            "Pressione uma tecla para jogar.", 1, GameSettings.GREEN)

        while True:

            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.centralized_text(title)
            self.screen.blit(click_text, (50, 50))

            if self.get_random_key() is not None:
                pygame.event.get()
                return

            pygame.display.update()

    def draw_score(self, snake):
        score_text = pygame.font.SysFont("hack", 15)
        score = score_text.render(
            "Score: " + self.score, 1, GameSettings.BLUE)
        self.screen.blit(score, (50, 50))

    def get_random_key(self):
        key_event = pygame.event.get(pygame.KEYUP)

        if len(key_event) == 0:
            return None

        if key_event[0].key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        return key_event[0].key

    def game_over_screen(self):
        game_over_font = pygame.font.SysFont("hack", 50)
        game_over_text = game_over_font.render(
            "Você morreu!", 1, GameSettings.BLUE)
        score_text = game_over_font.render(
            "Sua pontuação foi: " + self.score, 0, GameSettings.BLUE)
        score_text_width = score_text.get_rect().width
        click_font = pygame.font.SysFont("hack", 20)
        click_text = click_font.render(
            "Pressione uma tecla para jogar novamente.", 1, GameSettings.GREEN)
        self.screen.fill(GameSettings.BACKGROUND)

        while True:

            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.centralized_text(game_over_text)
            self.screen.blit(score_text, (
                (GameSettings.SCREEN_SIZE[0] / 2) - (score_text_width / 2),
                150))

            self.screen.blit(click_text, (50, 50))
            pygame.display.update()
            pygame.time.wait(1000)

            if self.get_random_key() is not None:
                pygame.event.get()
                return

            pygame.display.update()

    def run(self):
        pygame.init()
        snake = Snake()
        done = False
        clock = pygame.time.Clock()
        apple = Apple()

        self.set_caption()
        self.set_screen()

        self.show_title()

        while not done:
            clock.tick(10)

            self.set_screen()
            self.draw_background_chain()

            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()

            snake.draw(self.screen)
            snake.handle_keys()
            snake.set_direction()
            self.draw_score(snake)

            apple.draw(self.screen)

            # Checks if the player ate the apple.
            if snake.ate_apple(apple):
                apple = Apple()
                apple.draw(self.screen)
                snake.length += 1
                self.score = str(snake.length - 2)
                new_position = {"x": snake.coords[-1]["x"],
                                "y": snake.coords[-1]["y"]}
                snake.coords.append(new_position)

            # Checks if the snake hit itself.
            if snake.hit_itself():
                self.game_over_screen()
                snake = Snake()
                apple = Apple()
                self.score = "0"

            if snake.on_border():
                self.game_over_screen()
                snake = Snake()
                apple = Apple()
                self.score = "0"

            pygame.display.update()
