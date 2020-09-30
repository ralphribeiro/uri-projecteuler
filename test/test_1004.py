from unittest import TestCase
from exercicios.ex1004 import calcula_produto

class TesteEx1004(TestCase):
    def test_ambos_argumentos_devem_ser_int(self):
        with self.assertRaises(TypeError):
            calcula_produto(0.1, '')

    def test_produto_de_3_e_9_tem_que_ser_27(self):
        A = 3
        B = 9

        retorno = "PROD = 27"

        self.assertEqual(calcula_produto(A, B), retorno)

    def test_produto_de_menos_30_e_10_tem_que_ser_menos_300(self):
        A = -30
        B = 10

        retorno = "PROD = -300"

        self.assertEqual(calcula_produto(A, B), retorno)

    def test_produto_de_0_e_9_tem_que_ser_0(self):
        A = 0
        B = 9

        retorno = "PROD = 0"

        self.assertEqual(calcula_produto(A, B), retorno)