class Configurations:
    def __init__(self):
        self.variables = {"player_speed": 2,
                          "player_growth": 2,
                          "square_speed": 1,
                          "square_spawnrate": 0.02,
                          "square_directions": (True, False),
                          "window_size": (1000, 800)
        }

    def change_player_speed(self):
        speed = self.variables["player_speed"]
        if speed == 2:
            self.variables["player_speed"] = 4
        elif speed == 4:
            self.variables["player_speed"] = 6
        elif speed == 6:
            self.variables["player_speed"] = 2

    def change_player_growth(self):
        growth = self.variables["player_growth"]
        if growth == 2:
            self.variables["player_growth"] = 5
        elif growth == 5:
            self.variables["player_growth"] = 8
        elif growth == 8:
            self.variables["player_growth"] = 2

    def change_square_speed(self):
        speed = self.variables["square_speed"]
        if speed == 1:
            self.variables["square_speed"] = 2
        elif speed == 2:
            self.variables["square_speed"] = 3
        elif speed == 3:
            self.variables["square_speed"] = 4
        elif speed == 4:
            self.variables["square_speed"] = 5
        elif speed == 5:
            self.variables["square_speed"] = 1

    def change_square_spawnrate(self):
        spawnrate = self.variables["square_spawnrate"]
        if spawnrate == 0.02:
            self.variables["square_spawnrate"] = 0.05
        elif spawnrate == 0.05:
            self.variables["square_spawnrate"] = 0.1
        elif spawnrate == 0.1:
            self.variables["square_spawnrate"] = 0.15
        elif spawnrate == 0.15:
            self.variables["square_spawnrate"] = 0.2
        elif spawnrate == 0.2:
            self.variables["square_spawnrate"] = 0.02
