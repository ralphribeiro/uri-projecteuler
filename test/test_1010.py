from unittest import TestCase
from exercicios.ex1010 import calcula_total


class TesteEx1010(TestCase):
    def test_12_e_1_e_5v30_deve_ser_15v50(self):
        linha_um = '12 1 5.30'
        linha_dois = '16 2 5.10'
        esperado = 'VALOR A PAGAR: R$ 15.50'

        self.assertEqual(calcula_total(linha_um, linha_dois), esperado)

    def test_13_e_2_e_15v30_deve_ser_51v40(self):
        linha_um = '13 2 15.30'
        linha_dois = '161 4 5.20'
        esperado = 'VALOR A PAGAR: R$ 51.40'

        self.assertEqual(calcula_total(linha_um, linha_dois), esperado)

    def test_1_e_1_e_15v10_deve_ser_30v20(self):
        linha_um = '1 1 15.10'
        linha_dois = '2 1 15.10'
        esperado = 'VALOR A PAGAR: R$ 30.20'

        self.assertEqual(calcula_total(linha_um, linha_dois), esperado)
