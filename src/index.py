import pygame
from mainmenu import mainmenu
from game import game
from db.db_highscore import add_score

if __name__ == "__main__":
    start_game = mainmenu() #pylint: disable=invalid-name
    if start_game:
        SCORE = game()
        add_score("xxx", SCORE)
    pygame.quit()
