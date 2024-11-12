import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20)

    def test_ota_rahaa_vahenee(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)
        
    def test_ota_liikaa_rahaa(self):
        kortti = Maksukortti(100)
        
        self.assertEqual(kortti.ota_rahaa(200), False)
        self.assertEqual(kortti.saldo_euroina(), 1.0)
