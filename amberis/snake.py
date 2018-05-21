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
