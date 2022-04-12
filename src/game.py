import pygame

class Startgame:
    def __init__(self):
        self.game = True

    def main_menu():

        window_width = 900
        window_height = 600

        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("game has been quit")
                        running = False


    def platformer():

        screen = pygame.display.set_mode((900, 600))

Startgame.main_menu()