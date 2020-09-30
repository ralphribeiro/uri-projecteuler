from unittest import TestCase
from exercicios.ex1016 import calcula_distancia


class TesteEx1016(TestCase):
    def test_distancia_30_deve_ser_em_60_minutos(self):
        entrada = 30
        esperado = '60 minutos'

        self.assertEqual(calcula_distancia(entrada), esperado)

    def test_distancia_100_deve_ser_em_220_minutos(self):
        entrada = 110
        esperado = '220 minutos'

        self.assertEqual(calcula_distancia(entrada), esperado)

    def test_distancia_7_deve_ser_em_14_minutos(self):
        entrada = 7
        esperado = '14 minutos'

        self.assertEqual(calcula_distancia(entrada), esperado)
