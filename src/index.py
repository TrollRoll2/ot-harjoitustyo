import pygame
from configurations import Configurations
from menu import mainmenu, options_menu, nametracker
from game import game
from db.db_highscore import add_score

if __name__ == "__main__":
    CONFIGURATION = Configurations()
    while True:
        menu_choice = mainmenu(CONFIGURATION) #pylint: disable=invalid-name
        if menu_choice == "play":
            SCORE = game(CONFIGURATION)
            name = nametracker(SCORE, CONFIGURATION)
            if 0 < len(name) < 4:
                add_score(name, SCORE)
        elif menu_choice == "options":
            CONFIGURATION = options_menu(CONFIGURATION)
        elif menu_choice == "quit":
            break
    pygame.quit()
