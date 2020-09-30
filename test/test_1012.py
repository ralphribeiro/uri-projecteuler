from unittest import TestCase
from exercicios.ex1012 import calcula_area


class TesteEx1012(TestCase):
    def test_area_para_3v0_e_4v0_e_5v2_tem_que_ser_vide_tabela(self):
        """    	
            TRIANGULO: 7.800
            CIRCULO: 84.949
            TRAPEZIO: 18.200
            QUADRADO: 16.000
            RETANGULO: 12.000
        """
        linha = '3.0 4.0 5.2'

        esperado = 'TRIANGULO: 7.800\nCIRCULO: 84.949\nTRAPEZIO: 18.200\nQUADRADO: 16.000\nRETANGULO: 12.000'

        self.assertEqual(calcula_area(linha), esperado)

    def test_area_para_3v0_e_4v0_e_5v2_tem_que_ser_vide_tabela(self):
        """    	
            TRIANGULO: 96.520
            CIRCULO: 725.833
            TRAPEZIO: 175.560
            QUADRADO: 108.160
            RETANGULO: 132.080
        """
        linha = '12.7 10.4 15.2'

        esperado = 'TRIANGULO: 96.520\nCIRCULO: 725.833\nTRAPEZIO: 175.560\nQUADRADO: 108.160\nRETANGULO: 132.080'

        self.assertEqual(calcula_area(linha), esperado)
