from unittest import TestCase
from exercicios.ex1011 import calcula_volume_esfera


class TesteEx1011(TestCase):
    def test_volume_para_raio_3_tem_que_ser_113v097(self):
        r = 3
        esperado = 'VOLUME = 113.097'

        self.assertEqual(calcula_volume_esfera(r), esperado)

    def test_volume_para_raio_15_tem_que_ser_14137v155(self):
        r = 15
        esperado = 'VOLUME = 14137.155'

        self.assertEqual(calcula_volume_esfera(r), esperado)

    def test_volume_para_raio_1523_tem_que_ser_14797486501v627(self):
        r = 1523
        esperado = 'VOLUME = 14797486501.627'

        self.assertEqual(calcula_volume_esfera(r), esperado)
