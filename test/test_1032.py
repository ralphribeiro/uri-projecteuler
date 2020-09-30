from unittest import TestCase
from exercicios.ex1032 import encontra_sobrevivente


class TestEx1032(TestCase):
    def test_retonar_4_para_entrada_6(self):
        chamada = 6
        esperado = 4

        retorno = encontra_sobrevivente(chamada)

        self.assertEqual(esperado, retorno)