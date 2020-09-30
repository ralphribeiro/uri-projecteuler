from unittest import TestCase
from exercicios.ex1020 import calcula_idade_em_dias


class TesteEx1020(TestCase):
    def test_400_dever_retornar_1ano_1mes_5dia(self):
        chamada = 400
        esperado = '1 ano(s)\n1 mes(es)\n5 dia(s)'

        self.assertEqual(calcula_idade_em_dias(chamada), esperado)


    def test_800_dever_retornar_2ano_2mes_10dia(self):
        chamada = 800
        esperado = '2 ano(s)\n2 mes(es)\n10 dia(s)'

        self.assertEqual(calcula_idade_em_dias(chamada), esperado)

    
    def test_30_dever_retornar_0ano_1mes_0dia(self):
        chamada = 30
        esperado = '0 ano(s)\n1 mes(es)\n0 dia(s)'

        self.assertEqual(calcula_idade_em_dias(chamada), esperado)
