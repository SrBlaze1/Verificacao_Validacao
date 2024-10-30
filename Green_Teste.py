import unittest
from media import calcular_media  # Assumindo que o algoritmo ficará em um arquivo chamado media.py

class TestCalculoMedia(unittest.TestCase):
    def test_media_basica(self):
        self.assertAlmostEqual(calcular_media(7, 8, 9), 8.0)

    def test_media_notas_zero(self):
        self.assertAlmostEqual(calcular_media(0, 0, 0), 0.0)

    def test_media_notas_maximas(self):
        self.assertAlmostEqual(calcular_media(10, 10, 10), 10.0)

    def test_media_valores_decimais(self):
        self.assertAlmostEqual(calcular_media(6.5, 7.2, 8.3), 7.33, places=2)

if __name__ == '__main__':
    unittest.main()
