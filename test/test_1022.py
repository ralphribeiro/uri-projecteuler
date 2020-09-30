from unittest import TestCase
from exercicios.ex1022 import calcula_expressao


class TesteEx1022(TestCase):
    def test_expressao_tabela_tem_que_dar_tabela(self):
        chamada = '1 / 2 + 3 / 4'
        esperado = '5/4'

        self.assertEqual(calcula_expressao(chamada), esperado)

    def test_expressao_tabela_tem_que_dar_tabela(self):
        chamada = '1 / 2 - 3 / 4'
        esperado = '-1/4'

        self.assertEqual(calcula_expressao(chamada), esperado)

    def test_expressao_tabela_tem_que_dar_tabela(self):
        chamada = '2 / 3 * 6 / 6'
        esperado = '2/3'

        self.assertEqual(calcula_expressao(chamada), esperado)

    def test_expressao_tabela_tem_que_dar_tabela(self):
        chamada = '1 / 2 / 3 / 4'
        esperado = '2/3'

        self.assertEqual(calcula_expressao(chamada), esperado)
