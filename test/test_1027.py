from unittest import TestCase
from exercicios.ex1027 import encontra_pontos


class TesteEx1027(TestCase):
    def test_um(self):
        chamada = '10\n0 1\n1 0\n1 -1\n2 -2\n3 1\n3 -1\n3 -2\n4 1\n4 -1\n5 -1'
        esperado = '4'
        
        self.assertEqual(encontra_pontos(chamada), esperado)