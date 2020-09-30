from unittest import TestCase
from exercicios.ex1005 import calcula_media


class TestEx1005(TestCase):
    def test_ambos_argumentos_devem_ser_float(self):
        with self.assertRaises(TypeError):
            calcula_media(1, " ")

    def test_media_de_5_v_0_e_7_v_1_tem_que_ser_6_v_43182(self):
        A = 5.0
        B = 7.1

        esperado = 'MEDIA = 6.43182'

        self.assertEqual(calcula_media(A, B), esperado)

    def test_media_de_0_v_0_e_7_v_1_tem_que_ser_4_v_84091(self):
        A = 0.0
        B = 7.1

        esperado = 'MEDIA = 4.84091'

        self.assertEqual(calcula_media(A, B), esperado)

    def test_media_de_10_v_0_e_10_v_0_tem_que_ser_10_v_00000(self):
        A = 10.0
        B = 10.0

        esperado = 'MEDIA = 10.00000'

        self.assertEqual(calcula_media(A, B), esperado)
