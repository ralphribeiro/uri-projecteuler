from unittest import TestCase
from exercicios.ex1018 import calcula_numero_de_cedulas


class TesteEx1018(TestCase):
    def teste_da_caralha_toda(self):
        self.assertEqual(calcula_numero_de_cedulas(
            576), '576\n5 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n1 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n0 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00\n')

    def teste_da_caralha_toda_2(self):
        self.assertEqual(calcula_numero_de_cedulas(
            11257), '11257\n112 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n0 nota(s) de R$ 1,00\n')

    def teste_da_caralha_toda_2(self):
        self.assertEqual(calcula_numero_de_cedulas(
            503), '503\n5 nota(s) de R$ 100,00\n0 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n0 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00\n')
