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
