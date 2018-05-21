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

    def run(self):
        pygame.init()
        snake = Snake()
        done = False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(10)

            # Closes the window if the user clicked to close.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen = self.set_screen()
            snake.draw(screen)
            snake.handle_keys()
            block = Block()
            block.draw(screen)
            pygame.display.update()

        pygame.quit()
