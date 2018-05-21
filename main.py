import pygame

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_SIZE = [1200, 800]


class Block:

    def __init__(self):
        self.rect = pygame.rect.Rect((50, 50, 50, 50))
        self.value = 1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)


class Snake:

    def __init__(self):
        self.length = 1
        self.rect = pygame.rect.Rect((50, 50, 50, 50))

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
        pygame.draw.rect(screen, WHITE, self.rect)
        self.rect.clamp_ip(screen.get_rect())


class Game:

    def set_screen(self):
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Snake matemático")
        screen.fill(BACKGROUND)

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


game = Game()
game.run()
