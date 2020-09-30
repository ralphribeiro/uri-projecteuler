from unittest import TestCase
from exercicios.ex1028 import Ex1028


class TesteEx1028(TestCase):
    """Teste para o exercício 28."""

    def test_tamanho_maximo_pilha_259_e_111_deve_ser_37(self):
        x = 259
        y = 111
        esperado = 37
        
        ex1028 = Ex1028(x, y)
        retorno = ex1028.tamanho_maximo_pilha()
        self.assertEqual(esperado, retorno)

    def test_tamanho_maximo_pilha_9_e_27_deve_ser_9(self):
        x = 9
        y = 27
        esperado = 9
        
        ex1028 = Ex1028(x, y)
        retorno = ex1028.tamanho_maximo_pilha()
        self.assertEqual(esperado, retorno)

    def test_tamanho_maximo_pilha_259_e_111_deve_ser_4(self):
        x = 8
        y = 12
        esperado = 4
        
        ex1028 = Ex1028(x, y)
        retorno = ex1028.tamanho_maximo_pilha()
        self.assertEqual(esperado, retorno)