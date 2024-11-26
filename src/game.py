import pygame
from sprite import Sprite

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

def init_game():
    pygame.init()
    pygame.display.set_caption("Game hub")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def key_handler(key, player, screen_width, screen_height):
    if key[pygame.K_w]:
        player.move(0, -5, screen_width, screen_height)
    if key[pygame.K_a]:
        player.move(-5, 0, screen_width, screen_height)
    if key[pygame.K_s]:
        player.move(0, 5, screen_width, screen_height)
    if key[pygame.K_d]:
        player.move(5, 0, screen_width, screen_height)
    if key[pygame.K_ESCAPE]:
        return False

def screen_render(screen, player, font, score):
    screen.fill((0, 0, 0))
    player.draw(screen)
    scoretext = f"Score: {score}" #pylint: disable=invalid-name
    text_surface = font.render(scoretext, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topright=(SCREEN_WIDTH/2, 0))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def game():
    screen, clock = init_game()
    player = Sprite("src/images/smiley.png", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    font = pygame.font.Font(None, 30)
    score = 0
    running = True

    while running:
        running = event_handler()
        key = pygame.key.get_pressed()
        key_handler(key, player, SCREEN_WIDTH, SCREEN_HEIGHT)
        screen_render(screen, player, font, score)
        clock.tick(60)
    