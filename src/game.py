from random import random
import pygame
from player import Sprite
from square_generator import generate_square

def init_game(configuration):
    pygame.init()
    pygame.display.set_caption("Square game")
    screen_width, screen_height = configuration.variables["window_size"]
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    return screen, clock

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def key_handler(key, player, configuration):
    screen_width, screen_height = configuration.variables["window_size"]
    if key[pygame.K_w]:
        player.move(0, -configuration.variables["player_speed"], screen_width, screen_height)
    if key[pygame.K_a]:
        player.move(-configuration.variables["player_speed"], 0, screen_width, screen_height)
    if key[pygame.K_s]:
        player.move(0, configuration.variables["player_speed"], screen_width, screen_height)
    if key[pygame.K_d]:
        player.move(configuration.variables["player_speed"], 0, screen_width, screen_height)

def screen_render(screen, player, squares, score, configuration):
    screen_width, screen_height = configuration.variables["window_size"]
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 30)
    player.draw(screen)
    for square in squares:
        square.draw(screen)
    scoretext = f"Score: {score}"
    text_surface = font.render(scoretext, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(screen_width/2, 10))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def game(configuration):
    screen, clock = init_game(configuration)
    screen_width, screen_height = configuration.variables["window_size"]
    player = Sprite((screen_width/2, screen_height/2))
    squares = []
    score = 0
    running = True

    while running:
        running = event_handler()
        key = pygame.key.get_pressed()
        key_handler(key, player, configuration)
        for square in squares:
            if player.rect.colliderect(square.rect):
                if player.size > square.size:
                    score += square.size // 5
                    player.grow(configuration.variables["player_growth"])
                    square.collision = True
                else:
                    return score

        if random() < configuration.variables["square_spawnrate"]:
            new_square = generate_square(screen_width + player.size,
                                         player.size,
                                         configuration.variables["square_speed"])
            squares.append(new_square)
        squares = [square for square in squares if not square.move()]

        screen_render(screen, player, squares, score, configuration)
        clock.tick(60)

    return score
