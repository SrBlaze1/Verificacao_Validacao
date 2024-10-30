import unittest
from media import calcular_media

class TestCalculoMedia(unittest.TestCase):
    def test_media_basica(self):
        """Teste básico para verificar a média de notas inteiras."""
        self.assertAlmostEqual(calcular_media(7, 8, 9), 8.0, places=2)

    def test_media_notas_zero(self):
        """Teste para verificar a média quando todas as notas são zero."""
        self.assertAlmostEqual(calcular_media(0, 0, 0), 0.0, places=2)

    def test_media_notas_maximas(self):
        """Teste para verificar a média quando todas as notas são valores máximos."""
        self.assertAlmostEqual(calcular_media(10, 10, 10), 10.0, places=2)

    def test_media_valores_decimais(self):
        """Teste para verificar o cálculo da média com valores decimais."""
        self.assertAlmostEqual(calcular_media(6.5, 7.2, 8.3), 7.33, places=2)

    def test_valores_invalidos(self):
        """Teste para verificar o tratamento de entradas inválidas."""
        invalid_inputs = [
            ('a', 8, 9),
            (7, 'b', 9),
            (7, 8, 'c'),
            (None, 8, 9),
            ([7], 8, 9),
        ]
        for nota1, nota2, nota3 in invalid_inputs:
            with self.subTest(nota1=nota1, nota2=nota2, nota3=nota3):
                with self.assertRaises(ValueError):
                    calcular_media(nota1, nota2, nota3)

if __name__ == '__main__':
    unittest.main()
