import pygame

class Sprite:
    def __init__(self, sprite, coordinates):
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

    def move(self, x, y, max_x, max_y):
        if 0 <= self.rect.x + x <= max_x - self.rect.width:
             self.rect.x += x
        if 0 <= self.rect.y + y <= max_y - self.rect.height:
             self.rect.y += y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
