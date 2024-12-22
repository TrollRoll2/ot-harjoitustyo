import pygame

class Square:
    def __init__(self, color, size, movement, coordinates):
        self.color = color
        self.size = size
        self.movement = movement
        self.coordinates = coordinates
        self.collision = False
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.size, self.size)

    def move(self):
        self.coordinates = (
            self.coordinates[0] + self.movement[0],
            self.coordinates[1] + self.movement[1]
        )
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.size, self.size)

        if (self.coordinates[0] < -1000 or
            self.coordinates[0] > 3000 or
            self.coordinates[1] < -1000 or
            self.coordinates[1] > 3000 or
            self.collision == True):
            return True
        
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
