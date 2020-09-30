from unittest import TestCase
from exercicios.ex1029 import chamadas_recursivas


class TestEx1029(TestCase):
    def test_deve_ser_apresentado_uma_linha_com_padrao(self):
        esperado1 = "fib(5) = 14 calls = 5"
        esperado2 = "fib(4) = 8 calls = 3"
        chamada1 = chamadas_recursivas(5)
        chamada2 = chamadas_recursivas(4)

        self.assertEqual(esperado1, chamada1)
        self.assertEqual(esperado2, chamada2)
