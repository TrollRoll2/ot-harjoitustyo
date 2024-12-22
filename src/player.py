import pygame

class Sprite:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.color = (0, 0, 255)
        self.size = 45
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.size, self.size)
        self.rect.center = coordinates

    def move(self, x, y, max_x, max_y):
        if 0 <= self.rect.centerx + x <= max_x:
            self.rect.x += x
        if 0 <= self.rect.centery + y <= max_y:
            self.rect.y += y

    def grow(self, growth):
        self.size += growth
        old_center = self.rect.center
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = old_center

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
