from unittest import TestCase

from exercicios.ex1053 import (Caso, calcula_distancia_entre_pontos,
                               main, triagem_casos)


class TestEx1053(TestCase):
    def setUp(self) -> None:
        self.chamada = '2\n4\nA1 C2\nB3 C3\nC4 C2\nC2 D2\n2\nA1 A5\nE1 E5\n'
        self.esperado = 'Case 1: 8.24\nCase 2: ~x(\n'
        self.Caso = Caso

    def test_triagem_chamada_com_dois_casos_deve_ser_criado_lista_dois_objetos(self):
        esperado = 2
        retorno = triagem_casos(self.chamada)
        self.assertEqual(esperado, len(retorno))

    def test_triagem_chamada_com_dois_casos_deve_ser_criado_lista_dois_objetos_tipo_caso(self):
        retorno = triagem_casos(self.chamada)
        self.assertIsInstance(retorno[0], self.Caso)
        self.assertIsInstance(retorno[1], self.Caso)

    def test_caso_pontos_devem_ser_convertidos_pra_lista_lista_de_inteiros_com_os_valores(self):
        esperado_caso1 = ('linha:1, xa:1, ya:1, xa:2, yb:3, linha:2, xa:3, ya:2, xb:3, yb:3], '
                          'linha:3, xa:4, ya:3, xb:2, yb:3, linha:4, xa:2, ya:3, xb:2, yb:4')
        # esperado_caso2 = [[1, 1, 1, 5], [5, 1, 5, 5]]

        retorno = triagem_casos(self.chamada)

        self.assertEqual(esperado_caso1, retorno[0].linhas)
        # self.assertEqual(esperado_caso2, retorno[1].linhas)

    def test_calcula_distancia_entre_pontos(self):
        chamada1 = [1, 1, 3, 2]
        chamada2 = [2, 3, 3, 3]
        chamada3 = [3, 4, 3, 2]
        chamada4 = [3, 2, 4, 2]

        esperado1 = 2.24
        esperado2 = 1
        esperado3 = 2
        esperado4 = 1

        retorno1 = calcula_distancia_entre_pontos(chamada1)
        retorno2 = calcula_distancia_entre_pontos(chamada2)
        retorno3 = calcula_distancia_entre_pontos(chamada3)
        retorno4 = calcula_distancia_entre_pontos(chamada4)
        
        self.assertEqual(esperado1, retorno1)
        self.assertEqual(esperado2, retorno2)
        self.assertEqual(esperado3, retorno3)
        self.assertEqual(esperado4, retorno4)

    
    def test_chamada_deve_retornar_string(self):
        self.assertEqual(main(self.chamada), self.esperado)
        
