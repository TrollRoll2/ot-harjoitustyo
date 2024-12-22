import pygame
from menu import mainmenu, nametracker
from game import game
from db.db_highscore import add_score

if __name__ == "__main__":
    start_game = mainmenu() #pylint: disable=invalid-name
    if start_game:
        SCORE = game()
        name = nametracker(SCORE)
        if 0 < len(name) < 4:
            add_score(name, SCORE)
    pygame.quit()
