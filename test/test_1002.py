from unittest import TestCase
from exercicios.ex1002 import calcula_area_circunferencia


class TesteEx1002(TestCase):
    def test_argumento_deve_ser_float(self):
        chamada = 1
        with self.assertRaises(TypeError):
            calcula_area_circunferencia(chamada)

    def test_area_para_raio_0_ou_negativo_deve_ser_0(self):
        chamada = -1.00
        esperado = 0

        self.assertEqual(calcula_area_circunferencia(chamada), esperado)

    def test_area_de_2_v_00_deve_ser_12_v_5664(self):
        chamada = 2.00
        esperado = 'A = 12.5664'

        self.assertEqual(calcula_area_circunferencia(chamada), esperado)

    def test_area_de_100_v_64_deve_ser_31819_v_3103(self):
        chamada = 100.64
        esperado = 'A = 31819.3103'

        self.assertEqual(calcula_area_circunferencia(chamada), esperado)

    def test_area_de_150_v_00_deve_ser_70685_v_7750(self):
        chamada = 150.00
        esperado = 'A = 70685.7750'

        self.assertEqual(calcula_area_circunferencia(chamada), esperado)
