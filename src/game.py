import pygame
import os
from sprite import Sprite

pygame.init()

pygame.display.set_caption("Game hub")
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
player = Sprite("src/smiley.png", (screen_width/2, screen_height/2))
score = 0
font = pygame.font.Font(None, 20)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move(0, -5, screen_width, screen_height)
        score += 1
    if key[pygame.K_a]:
        player.move(-5, 0, screen_width, screen_height)
        score += 1
    if key[pygame.K_s]:
        player.move(0, 5, screen_width, screen_height)
        score += 1
    if key[pygame.K_d]:
        player.move(5, 0, screen_width, screen_height)
        score += 1

    screen.fill((0, 0, 0))
    player.draw(screen)
    scoretext = f"Score: {score}"
    text_surface = font.render(scoretext, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topright=(screen_width/2, 0)) 
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


