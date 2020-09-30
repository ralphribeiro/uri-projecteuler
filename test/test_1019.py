from unittest import TestCase
from exercicios.ex1019 import converte_tempo

class TesteEx1019(TestCase):
    def test_para_entrada_556_a_saida_deve_ser_0h9m16s(self):
        entrada = 556
        esperado = '0:9:16'
        self.assertEqual(converte_tempo(entrada), esperado)


    def test_para_entrada_1_a_saida_deve_ser_0h0m1s(self):
        entrada = 1
        esperado = '0:0:1'
        self.assertEqual(converte_tempo(entrada), esperado)


    def test_para_entrada_140153_a_saida_deve_ser_38h55m53s(self):
        entrada = 140153
        esperado = '38:55:53'
        self.assertEqual(converte_tempo(entrada), esperado)