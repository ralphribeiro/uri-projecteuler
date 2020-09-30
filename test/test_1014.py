from unittest import TestCase
from exercicios.ex1014 import calcula_consumo


class TesteEx1014(TestCase):
    def test_500km_com_35v5litros_tem_que_ter_o_consumo_14v286(self):
        dados = [500, 35.0]
        esperado = '14.286 km/l'

        self.assertEqual(calcula_consumo(dados), esperado)

    def test_2254km_com_124v4litros_tem_que_ter_o_consumo_18v119(self):
        dados = [2254, 124.4]
        esperado = '18.119 km/l'

        self.assertEqual(calcula_consumo(dados), esperado)

    def test_4554km_com_464v6litros_tem_que_ter_o_consumo_9v802(self):
        dados = [4554, 464.6]
        esperado = '9.802 km/l'

        self.assertEqual(calcula_consumo(dados), esperado)
