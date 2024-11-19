import unittest
from sprite import Sprite

class TestSpriteCollision(unittest.TestCase):
    def setUp(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.sprite = Sprite("src/smiley.png", (1, 1))

    def test_collision_top(self):
        self.sprite.move(0, -5, self.screen_width, self.screen_height)
        self.assertEqual(self.sprite.rect.top, 1)

if __name__ == "__main__":
    unittest.main()