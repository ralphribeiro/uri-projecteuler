from unittest import TestCase
from exercicios.ex1006 import calcula_media


class TesteEx1006(TestCase):
    def test_argumentos_devem_ser_float(self):
        with self.assertRaises(TypeError):
            calcula_media('', 1, 2)

    def test_media_de_5_v_0_e_6_v_0_e_7_v_0_tem_que_ser_6_v_3(self):
        A = 5.0
        B = 6.0
        C = 7.0
        esperado = 'MEDIA = 6.3'

        self.assertEqual(calcula_media(A, B, C), esperado)

    def test_media_de_5_v_0_e_10_v_0_e_10_v_0_tem_que_ser_9_v_0(self):
        A = 5.0
        B = 10.0
        C = 10.0
        esperado = 'MEDIA = 9.0'

        self.assertEqual(calcula_media(A, B, C), esperado)

    def test_media_de_10_v_0_e_10_v_0_e_5_v_0_tem_que_ser_7_v_5(self):
        A = 10.0
        B = 10.0
        C = 5.0
        esperado = 'MEDIA = 7.5'

        self.assertEqual(calcula_media(A, B, C), esperado)
