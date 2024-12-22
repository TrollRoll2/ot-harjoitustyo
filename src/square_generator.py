from random import randint, random
from square import Square

def generate_square(max, player_size, square_speed):
    direction = ((1 if random() < 0.5 else -1,
                  1 if random() < 0.5 else -1))
    return Square((randint(30, 255), randint(30, 255), randint(30, 255)),
                    randint(player_size - 45, player_size + 45),
                    (square_speed*direction[0], 0),
                    (-player_size if direction[0] > 0 else max, randint(0, 800))
            )
