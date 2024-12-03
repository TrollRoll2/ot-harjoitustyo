from random import randint
import pygame

class Enemy:
    def __init__(self, enemy, coordinates):
        self.image = pygame.image.load(enemy)
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

    def respawn(self, player_rect, max_x, max_y):
        while True:
            x = randint(0, max_x - self.rect.width)
            y = randint(0, max_y- self.rect.height)
            if not player_rect.colliderect(pygame.Rect(x, y, self.rect.width, self.rect.height)):
                self.rect.topleft = (x, y)
                break

    def draw(self, screen):
        screen.blit(self.image, self.rect)
