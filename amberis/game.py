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
import random

import pygame

from apple import Apple
from snake import Snake
from settings import GameSettings


class Game:
    """Base class to run the game.
    """

    def __init__(self):
        self.score = "0"
        self.screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE)
        self.eaten_apples = []

    def set_caption(self):
        """Sets the caption. """
        pygame.display.set_caption("Snake matemático")

    def set_screen(self):
        """Sets the screen to be filled with green. """
        self.screen.fill(GameSettings.LIGHT_GREEN)

    def draw_background_chain(self):
        """Draws the background chain. """
        for line in range(0,
                          GameSettings.SCREEN_SIZE[0],
                          GameSettings.CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GameSettings.LIGHT_BLUE, (line, 0),
                (line, GameSettings.SCREEN_SIZE[1]))

        for column in range(0,
                            GameSettings.SCREEN_SIZE[1],
                            GameSettings.CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GameSettings.LIGHT_BLUE, (0, column),
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
        """Displays the title. """
        title_font = pygame.font.SysFont("hack", 100)
        title = title_font.render("Amberis", 1, GameSettings.WHITE)

        click_font = pygame.font.SysFont("hack", 20)
        click_text = click_font.render(
            "Pressione uma tecla para jogar.", 1, GameSettings.RED)
        tutorial_text = click_font.render(
            '''
            O jogo consiste em após comer dois números consectutivos,
            o terceiro deve ser a soma dos anteriores.
            ''',
            1, GameSettings.WHITE)

        while True:
            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.centralized_text(title)
            tutorial_text_width = tutorial_text.get_rect().width
            self.screen.blit(tutorial_text, (
                GameSettings.SCREEN_WIDTH / 2 - tutorial_text_width / 2,
                500
            ))
            self.screen.blit(click_text, (50, 50))

            if self.get_random_key() is not None:
                pygame.event.get()
                return 0

            pygame.display.update()

    def draw_score(self, snake):
        score_text = pygame.font.SysFont("hack", 15)
        score = score_text.render(
            "Score: " + self.score, 1, GameSettings.BLUE)
        self.screen.blit(score, (50, 50))

    def get_random_key(self):
        key_event = pygame.key.get_pressed()

        if key_event[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for i in key_event:
            if i != 0:
                return key_event

        return None

    def game_over_screen(self):
        game_over_font = pygame.font.SysFont("hack", 50)
        game_over_text = game_over_font.render(
            "Você morreu!", 1, GameSettings.BLUE)
        score_text = game_over_font.render(
            "Sua pontuação foi: " + self.score, 0, GameSettings.BLUE)
        score_text_width = score_text.get_rect().width
        click_font = pygame.font.SysFont("hack", 20)
        click_text = click_font.render(
            "Pressione uma tecla para jogar novamente.", 1, GameSettings.RED)
        self.set_screen()

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
                return

            pygame.display.update()

    def run(self):
        pygame.init()
        snake = Snake()
        done = False
        clock = pygame.time.Clock()
        apple0 = Apple()
        apple1 = Apple()
        apple2 = Apple()
        apple3 = Apple(sum(self.eaten_apples))
        apples = [apple0, apple1, apple2, apple3]

        self.set_caption()
        self.set_screen()

        self.show_title()

        while not done:
            clock.tick(15)

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

            if len(self.eaten_apples) == 2:
                for apple in apples[1:]:
                    apple.draw(self.screen)
            else:
                apples[0].draw(self.screen)

            # Checks if the player ate the apple.
            for apple in apples:
                if snake.ate_apple(apple) and apple.drawn:
                    self.eaten_apples.append(apple.value)
                    if len(self.eaten_apples) == 2:
                        apples[0] = Apple()
                        apples[1] = Apple(
                            sum(self.eaten_apples) +
                            random.randint(1, 5))
                        apples[2] = Apple(
                            sum(self.eaten_apples) +
                            random.randint(1, 5))
                        apples[3] = Apple(sum(self.eaten_apples))

                        apples[1].draw(self.screen)
                        apples[2].draw(self.screen)
                        apples[3].draw(self.screen)

                    elif len(self.eaten_apples) == 3:
                        if (apple.value ==
                                self.eaten_apples[0] + self.eaten_apples[1]):
                            self.eaten_apples.clear()
                            snake.length += 1
                            self.score = str(snake.length - 2)
                            new_position = {"x": snake.coords[-1]["x"],
                                            "y": snake.coords[-1]["y"]}
                            snake.coords.append(new_position)
                        else:
                            self.eaten_apples.clear()
                            self.game_over_screen()
                            snake = Snake()
                            apples[0] = Apple()
                            apples[1] = Apple()
                            apples[2] = Apple()
                            apples[3] = Apple()
                            self.score = "0"
                    else:
                        apples[0] = Apple()
                        apples[0].draw(self.screen)

            # Checks if the snake hit itself.
            if snake.hit_itself() or snake.on_border():
                self.eaten_apples.clear()
                self.game_over_screen()
                snake = Snake()
                apples[0] = Apple()
                apples[1] = Apple()
                apples[2] = Apple()
                apples[3] = Apple()
                self.score = "0"

            pygame.display.update()
