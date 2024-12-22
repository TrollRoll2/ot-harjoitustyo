from random import randint, random
import pygame
from player import Sprite
from square_generator import generate_square

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

def init_game():
    pygame.init()
    pygame.display.set_caption("Square game")
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
        player.move(0, -2, screen_width, screen_height)
    if key[pygame.K_a]:
        player.move(-2, 0, screen_width, screen_height)
    if key[pygame.K_s]:
        player.move(0, 2, screen_width, screen_height)
    if key[pygame.K_d]:
        player.move(2, 0, screen_width, screen_height)
    if key[pygame.K_ESCAPE]:
        return False

def screen_render(screen, player, squares, font, score):
    screen.fill((255, 255, 255))
    player.draw(screen)
    for square in squares:
        square.draw(screen)
    scoretext = f"Score: {score}"
    text_surface = font.render(scoretext, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, 10))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def game():
    screen, clock = init_game()
    player = Sprite((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    squares = []
    font = pygame.font.Font(None, 30)
    score = 0
    running = True

    while running:
        running = event_handler()
        key = pygame.key.get_pressed()
        key_handler(key, player, SCREEN_WIDTH, SCREEN_HEIGHT)
        for square in squares:
            if player.rect.colliderect(square.rect):
                if player.size > square.size:
                    score += square.size // 5
                    player.grow(2)
                    square.collision = True
                else:
                    return score
                
        if random() < 0.02:
            new_square = generate_square(SCREEN_WIDTH + player.size, player.size)
            squares.append(new_square)
        squares = [square for square in squares if not square.move()]

        screen_render(screen, player, squares, font, score)
        clock.tick(60)

    return score
