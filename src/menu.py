import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

def init_menu():
    pygame.init()
    pygame.display.set_caption("Main menu")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock

def button(screen, text, font, color, rect):
    pygame.draw.rect(screen, color, rect)
    button_text = font.render(text, True, (255, 255, 255))
    button_outline = button_text.get_rect(center=rect.center)
    screen.blit(button_text, button_outline)

def mainmenu():
    screen, clock = init_menu()
    font = pygame.font.Font(None, 50)
    play_button = pygame.Rect(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT*(1/2) - 150, 400, 100)
    options_button = pygame.Rect(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT*(1/2), 400, 100)
    exit_button = pygame.Rect(SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT*(1/2) + 150, 400, 100)
    running = True

    while running:
        screen.fill((255, 255, 255))
        button(screen, "Play", font, (0, 0, 0), play_button)
        button(screen, "Options", font, (0, 0, 0), options_button)
        button(screen, "Exit", font, (0, 0, 0), exit_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return True
                if exit_button.collidepoint(event.pos):
                    return False
                
        pygame.display.flip()
        clock.tick(60)

def nametracker(score):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    banner = pygame.Rect(SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT*(1/2) - 100, 600, 50)
    input_box = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT*(1/2), 200, 50)
    submit_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT*(1/2) + 100, 200, 50)
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
