from random import randint, random
from square import Square

def generate_square(max, player_size, spread=40):
    direction = ((1 if random() < 0.5 else -1,
                  1 if random() < 0.5 else -1))
    return Square((randint(30, 255), randint(30, 255), randint(30, 255)),
                    randint(player_size - spread, player_size + spread),
                    (1*direction[0], 0),
                    (-player_size if direction[0] > 0 else max, randint(0, 800))
            )
