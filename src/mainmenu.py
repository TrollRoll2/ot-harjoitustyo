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
    button_text = font.render(text, True, (0, 0, 0))
    button_outline = button_text.get_rect(center=rect.center)
    screen.blit(button_text, button_outline)

def mainmenu():
    screen, clock = init_menu()
    font = pygame.font.Font(None, 50)
    play_button = pygame.Rect(400, 200, 300, 100)
    exit_button = pygame.Rect(400, 400, 300, 100)
    running = True

    while running:
        screen.fill((0, 0, 0))
        button(screen, "Play", font, (255, 255, 255), play_button)
        button(screen, "Exit", font, (255, 255, 255), exit_button)

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
