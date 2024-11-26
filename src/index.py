import pygame
from mainmenu import mainmenu
from game import game

if __name__ == "__main__":
    start_game = mainmenu() #pylint: disable=invalid-name
    if start_game:
        game()
    pygame.quit()
