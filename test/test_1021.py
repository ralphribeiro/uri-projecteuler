from unittest import TestCase
from exercicios.ex1021 import calcula_notas_moedas


class TesteEx1021(TestCase):
    def test_teste_retorno_para_576v73_tem_que_ser_vide_tabela(self):
        chamada = 576.73
        esperado = '100: 5\n50: 1\n20: 1\n10: 0\n5: 1\n2: 0\n1: 1\n0.5: 1\n0.25: 0\n0.1: 2\n0.05: 0\n0.01: 3\n'
        self.assertEqual(calcula_notas_moedas(chamada), esperado)


    def test_teste_retorno_para_4v00_tem_que_ser_vide_tabela(self):
        chamada = 4
        esperado = '100: 0\n50: 0\n20: 0\n10: 0\n5: 0\n2: 2\n1: 0\n0.5: 0\n0.25: 0\n0.1: 0\n0.05: 0\n0.01: 0\n'
        self.assertEqual(calcula_notas_moedas(chamada), esperado)

    def test_teste_retorno_para_91v01_tem_que_ser_vide_tabela(self):
        chamada = 91.01
        esperado = '100: 0\n50: 1\n20: 2\n10: 0\n5: 0\n2: 0\n1: 1\n0.5: 0\n0.25: 0\n0.1: 0\n0.05: 0\n0.01: 1\n'
        self.assertEqual(calcula_notas_moedas(chamada), esperado)