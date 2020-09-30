from unittest import TestCase
from exercicios.ex1009 import calcula_salario_com_bonus


class TesteEx1009(TestCase):
    def test_JOAO_500v00_1230v30_deve_ser_684v54(self):
        nome = 'JOAO'
        salario_fixo = 500.00
        montante_vendas = 1230.30
        esperado = 'TOTAL = R$ 684.54'

        self.assertEqual(calcula_salario_com_bonus(
            nome, salario_fixo, montante_vendas), esperado)

    def test_PEDRO_700v00_0v0_deve_ser_700v00(self):
        nome = 'PEDRO'
        salario_fixo = 700.00
        montante_vendas = 0.0
        esperado = 'TOTAL = R$ 700.00'

        self.assertEqual(calcula_salario_com_bonus(
            nome, salario_fixo, montante_vendas), esperado)

    def test_MANGOJATA_1700v00_1230v50_deve_ser_1884v58(self):
        nome = 'MANGOJATA'
        salario_fixo = 1700.00
        montante_vendas = 1230.50
        esperado = 'TOTAL = R$ 1884.58'

        self.assertEqual(calcula_salario_com_bonus(
            nome, salario_fixo, montante_vendas), esperado)
