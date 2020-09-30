from unittest import TestCase
from exercicios.ex1007 import calcula_diferenca


class TesteEx1007(TestCase):
    def test_argumentos_tem_que_ser_int(self):
        with self.assertRaises(TypeError):
            calcula_diferenca('', 2, 1.1, 3)

    def test_diferenca_entre_5_6_7_8_tem_que_ser_menos_26(self):
        A = 5
        B = 6
        C = 7
        D = 8
        esperado = 'DIFERENCA = -26'

        self.assertEqual(calcula_diferenca(A, B, C, D), esperado)

    def test_diferenca_entre_0_0_7_8_tem_que_ser_menos_56(self):
        A = 0
        B = 0
        C = 7
        D = 8
        esperado = 'DIFERENCA = -56'

        self.assertEqual(calcula_diferenca(A, B, C, D), esperado)

    def test_diferenca_entre_5_6_7_8_tem_que_ser_86(self):
        A = 5
        B = 6
        C = - 7
        D = 8
        esperado = 'DIFERENCA = 86'

        self.assertEqual(calcula_diferenca(A, B, C, D), esperado)
