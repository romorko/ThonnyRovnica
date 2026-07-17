#Testovanie triedy Rovnica
import unittest					#trieda obsahujuca testovacie metody
from math import isinf, isnan	#pre typ inf a nan
from main_v6a import  Rovnica	#trieda Rovnica ktoru testujeme

class TestRovnica(unittest.TestCase):#dedime z triedy jednotlive assertacie aj pomocne metody

    def test_nastavenie_hodnot_konstruktorom(self):
        r = Rovnica(10,27)		#vytvorí objekt rovnice
        self.assertEqual(r.a,10)
        self.assertEqual(r.b,27)
        
    def test_daj_riesenie_bezna_rovnica(self):
        r = Rovnica(10, 20)    # 10x + 20 = 0 -> x = -2
        self.assertEqual(r.dajRiesenie(), -2.0)
        
    def test_daj_riesenie_nulove_b(self):
        r = Rovnica(5, 0)      # 5x = 0 -> x = 0
        self.assertEqual(r.dajRiesenie(), 0.0)

    def test_daj_riesenie_nekonecne_vela_rieseni(self):
        r = Rovnica(0, 0)      # 0x + 0 = 0 -> veľa riešení
        self.assertTrue(isinf(r.dajRiesenie()))

    def test_daj_riesenie_ziadne_riesenie(self):
        r = Rovnica(0, 5)      # 0x + 5 = 0 -> bez riešenia
        self.assertTrue(isnan(r.dajRiesenie()))
        
    def test_str_kladne_b(self):
        r = Rovnica(10, 27)
        self.assertEqual(str(r), "10x + 27 = 0")

    def test_str_zaporne_b(self):
        r = Rovnica(10, -27)
        self.assertEqual(str(r), "10x - 27 = 0")
        
        
if __name__ == "__main__":
    unittest.main()
