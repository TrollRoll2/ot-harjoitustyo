import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
<<<<<<< HEAD
        self.assertNotEqual(self.maksukortti, None)
=======
        self.assertNotEqual(self.maksukortti, None)

    
>>>>>>> tmp
