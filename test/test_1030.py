from unittest import TestCase
from exercicios.ex1030 import calcula_suicidio

import random


class TestEx1030(TestCase):
    def test_saida_com_erro_para_entradas_fora_do_intervalo(self):
        chamada = [(0, 10), (10, 0), (10001, 10), (10, 1001)]

        esperado = ("Case 1: entrada inválida\n"
                    "Case 2: entrada inválida\n"
                    "Case 3: entrada inválida\n"
                    "Case 4: entrada inválida\n")

        retorno = calcula_suicidio(chamada)

        self.assertEqual(esperado, retorno)

    def test_saida_deve_retornar_case_1_3_para_entrada_5_2(self):
        chamada = [(5, 2), (6, 3), (1234, 233)]
        esperado = ("Case 1: 3\n"
                    "Case 2: 1\n"
                    "Case 3: 25\n")

        retorno = calcula_suicidio(chamada)

        self.assertEqual(esperado, retorno)
