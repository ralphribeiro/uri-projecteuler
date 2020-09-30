from unittest import TestCase
from exercicios.ex1013 import obtem_maior_em_lista


class TesteEx1013(TestCase):
    def test_o_maior_entre_7_e_14_106_tem_que_ser_106(self):
        lista = [7, 14, 106]
        esperado = '106 é o maior'

        self.assertEqual(obtem_maior_em_lista(lista), esperado)

    def test_o_maior_entre_207_14_6_tem_que_ser_217(self):
        lista = [217, 14, 6]
        esperado = '217 é o maior'

        self.assertEqual(obtem_maior_em_lista(lista), esperado)
