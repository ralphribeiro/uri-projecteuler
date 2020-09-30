from unittest import TestCase
from exercicios.ex1001 import calcula_soma


class TesteEx1001(TestCase):
    def test_ambos_argumentos_devem_ser_int(self):
        with self.assertRaises(TypeError):
            calcula_soma(1.1, 1)

    def test_soma_de_10_mais_9_tem_que_ser_19(self):
        A = 10
        B = 9
        esperado = "X = 19"

        self.assertEqual(calcula_soma(A, B), esperado)

    def test_soma_de_menos_10_mais_4_tem_que_ser_menos_6(self):
        A = -10
        B = 4
        esperado = 'X = -6'

        self.assertEqual(calcula_soma(A, B), esperado)

    def test_soma_de_15_mais_menos_7_tem_que_ser_8(self):
        A = 15
        B = -7
        esperado = 'X = 8'

        self.assertEqual(calcula_soma(A, B), esperado)
