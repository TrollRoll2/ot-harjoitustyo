import pygame
from sprite import Sprite

pygame.init() # pylint: disable=no-member

pygame.display.set_caption("Game hub")
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Sprite("src/smiley.png", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
score = 0 # pylint: disable=invalid-name
font = pygame.font.Font(None, 20)
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            RUNNING = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]: # pylint: disable=no-member
        player.move(0, -5, SCREEN_WIDTH, SCREEN_HEIGHT)
        score += 1 # pylint: disable=invalid-name
    if key[pygame.K_a]: # pylint: disable=no-member
        player.move(-5, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        score += 1 # pylint: disable=invalid-name
    if key[pygame.K_s]: # pylint: disable=no-member
        player.move(0, 5, SCREEN_WIDTH, SCREEN_HEIGHT)
        score += 1 # pylint: disable=invalid-name
    if key[pygame.K_d]: # pylint: disable=no-member
        player.move(5, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        score += 1 # pylint: disable=invalid-name
    if key[pygame.K_ESCAPE]: # pylint: disable=no-member
        RUNNING = False


    screen.fill((0, 0, 0))
    player.draw(screen)
    scoretext = f"Score: {score}" # pylint: disable=invalid-name
    text_surface = font.render(scoretext, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topright=(SCREEN_WIDTH/2, 0))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.QUIT() # pylint: disable=no-member
