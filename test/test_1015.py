from unittest import TestCase
from exercicios.ex1015 import calcula_distancia_entre_dois_pontos


class TesteEx1015(TestCase):
    def test_distancia_entre_os_pontos_1v0_e_7v0_com_5v0_e_9v0_tem_que_ser_4v4721(self):
        ponto_A = [1.0, 7.0]
        ponto_B = [5.0, 9.0]
        esperado = '4.4721'

        self.assertEqual(calcula_distancia_entre_dois_pontos(
            ponto_A, ponto_B), esperado)
