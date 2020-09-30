from unittest import TestCase

from exercicios.ex1034 import calcula_blocos


class TestEx1034(TestCase):
    def test_saida(self):
        esperado = '2\n23\n'
        chamada = '2\n6 100\n1 5 10 15 25 50\n2 103\n1 5'

        retorno = calcula_blocos(chamada)

        self.assertEqual(esperado, retorno)