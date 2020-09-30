from unittest import TestCase
from exercicios.ex1003 import calcula_soma


class TesteEx1003(TestCase):
    def test_ambos_argumentos_devem_ser_int(self):
        with self.assertRaises(TypeError):
            calcula_soma(1.1, 1)

    def test_soma_de_30_mais_10_tem_que_ser_40(self):
        A = 30
        B = 10
        esperado = "SOMA = 40"

        self.assertEqual(calcula_soma(A, B), esperado)

    def test_soma_de_menos_30_mais_10_tem_que_ser_20(self):
        A = -30
        B = 10
        esperado = 'SOMA = -20'

        self.assertEqual(calcula_soma(A, B), esperado)

    def test_soma_de_0_mais_0_tem_que_ser_0(self):
        A = 0
        B = 0
        esperado = 'SOMA = 0'

        self.assertEqual(calcula_soma(A, B), esperado)
