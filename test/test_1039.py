from unittest import TestCase
from exercicios.ex1039 import calcula_raio


class TestEx1039(TestCase):
    def test_saida_ex_1039(self):
        chamada = (
            '6 -8 2 3 0 0\n'
            '7 3 4 2 4 5\n'
            '3 0 0 4 0 0\n'
            '5 4 7 1 8 7\n'
        )
        esperado = (
            'MORTO\n'
            'RICO\n'
            'MORTO\n'
            'RICO\n'
        )

        retorno = calcula_raio(chamada)

        self.assertEqual(esperado, retorno)
