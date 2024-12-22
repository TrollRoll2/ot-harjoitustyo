import pygame
from db.db_highscore import highscores

def init_menu(configuration):
    screen_width, screen_height = configuration.variables["window_size"]
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    return screen, clock

def button(screen, text, font, color, rect):
    pygame.draw.rect(screen, color, rect)
    button_text = font.render(text, True, (255, 255, 255))
    button_outline = button_text.get_rect(center=rect.center)
    screen.blit(button_text, button_outline)

def options_menu(configuration):
    pygame.display.set_caption("Options")
    screen, clock = init_menu(configuration)
    font = pygame.font.Font(None, 50)
    screen_width, screen_height = configuration.variables["window_size"]
    player_speed_button = pygame.Rect(screen_width/3,
                                      screen_height*(1/6),
                                      400,
                                      100)
    player_growth_button = pygame.Rect(screen_width/3,
                                       screen_height*(1/3),
                                       400,
                                       100)
    square_speed_button = pygame.Rect(screen_width/3,
                                      screen_height*(1/2),
                                      400,
                                      100)
    square_spawnrate_button = pygame.Rect(screen_width/3,
                                          screen_height*(2/3),
                                          400,
                                          100)
    menu_button = pygame.Rect(screen_width/3,
                              screen_height*(5/6),
                              400,
                              100)
    running = True
    while running:
        screen.fill((255, 255, 255))
        button(screen, f"Player speed: {configuration.variables["player_speed"]}",
               font, (0, 0, 0), player_speed_button)
        button(screen, f"Player growth: {configuration.variables["player_growth"]}",
               font, (0, 0, 0), player_growth_button)
        button(screen, f"Square speed: {configuration.variables["square_speed"]}",
               font, (0, 0, 0), square_speed_button)
        button(screen, f"Square spawnrate: {configuration.variables["square_spawnrate"]}",
               font, (0, 0, 0), square_spawnrate_button)
        button(screen, "Back to Main Menu", font, (0, 0, 0), menu_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    return configuration
                if player_speed_button.collidepoint(event.pos):
                    configuration.change_player_speed()
                if player_growth_button.collidepoint(event.pos):
                    configuration.change_player_growth()
                if square_speed_button.collidepoint(event.pos):
                    configuration.change_square_speed()
                if square_spawnrate_button.collidepoint(event.pos):
                    configuration.change_square_spawnrate()

        pygame.display.flip()
        clock.tick(60)

    return None

def mainmenu(configuration):
    pygame.display.set_caption("Main menu")
    screen, clock = init_menu(configuration)
    font = pygame.font.Font(None, 50)
    screen_width, screen_height = configuration.variables["window_size"]
    play_button = pygame.Rect(screen_width/2 - 200, screen_height*(1/2) - 50, 400, 100)
    options_button = pygame.Rect(screen_width/2 - 200, screen_height*(1/2) + 100, 400, 100)
    exit_button = pygame.Rect(screen_width/2 - 200, screen_height*(1/2) + 250, 400, 100)
    highscore_label = pygame.Rect(screen_width/2 - 200, 10, 400, 100)
    running = True

    while running:
        screen.fill((255, 255, 255))
        button(screen, "Play", font, (0, 0, 0), play_button)
        button(screen, "Options", font, (0, 0, 0), options_button)
        button(screen, "Exit", font, (0, 0, 0), exit_button)
        button(screen, "Highscores:", font, (0, 0, 0), highscore_label)
        scorelist = highscores()
        separator = 125
        for score_id, score in enumerate(scorelist):
            score_text = f"{score_id + 1}. {score['player']}: {score['score']}"
            text_surface = pygame.font.Font(None, 30).render(score_text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(screen_width/2, separator))
            screen.blit(text_surface, text_rect)
            separator += 25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return "play"
                if options_button.collidepoint(event.pos):
                    return "options"
                if exit_button.collidepoint(event.pos):
                    return "quit"

        pygame.display.flip()
        clock.tick(60)

    return None

def nametracker(score, configuration):
    pygame.display.set_caption("Game finished")
    screen, clock = init_menu(configuration)
    font = pygame.font.Font(None, 50)
    screen_width, screen_height = configuration.variables["window_size"]
    banner = pygame.Rect(screen_width/2 - 300, screen_height*(1/2) - 100, 600, 50)
    input_box = pygame.Rect(screen_width/2 - 100, screen_height*(1/2), 200, 50)
    submit_button = pygame.Rect(screen_width/2 - 100, screen_height*(1/2) + 100, 200, 50)
    bannertext = f"You recieved {score} points! Enter a name below if you wish to submit:"
    text = ''
    running = True

    while running:
        screen.fill((255, 255, 255))
        button(screen, bannertext, pygame.font.Font(None, 25), (0, 0, 255), banner)
        button(screen, text, font, (0, 0, 0), input_box)
        button(screen, "Submit", font, (0, 0, 0), submit_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return ""
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.collidepoint(event.pos):
                    return text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(text) <= 3:
                        return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif len(text) < 3:
                    text += event.unicode

        pygame.display.flip()
        clock.tick(60)

    return None
