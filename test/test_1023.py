from unittest import TestCase
from exercicios.ex1023 import calcula_estiagem


class TesteEx1023(TestCase):
    def test_arquivo_invalido(self):
        chamada = 'xxx'
        esperado = 'arquivo inválido'

        self.assertEqual(calcula_estiagem(chamada), esperado)

    def test_arquivo_inexistente(self):
        chamada = 'arquibo.txt'
        esperado = 'arquivo inexistente'

        self.assertEqual(calcula_estiagem(chamada), esperado)

    def test_arquivo_valido_gera_primeiro_elemento_da_lista_a_cidade(self):
        chamada = 'ex1023.txt'
        esperado = '3'

        self.assertEqual(calcula_estiagem(chamada)[0:3], 'C#1')

    # def test_arquivo_valido_gera
