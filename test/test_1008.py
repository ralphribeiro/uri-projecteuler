from unittest import TestCase
from typing import NewType, Any
from exercicios.ex1008 import calcula_salario


Dummy = NewType('Dummy', Any)


class TesteEx1008(TestCase):

    def test_primeiro_argumento_deve_ser_inteiro(self):
        with self.assertRaises(TypeError):
            calcula_salario(1.0, Dummy, Dummy)

    def test_segundo_argumento_deve_ser_inteiro(self):
        with self.assertRaises(TypeError):
            calcula_salario(Dummy, " ", Dummy)

    def test_terceiro_argumento_deve_ser_float(self):
        with self.assertRaises(TypeError):
            calcula_salario(Dummy, Dummy, 1)

    def test_saida_para_funcionario_25_com_horas_100_e_valorhora_5_v_5_deve_ser_550_v_00(self):
        funcionario = 25
        horas_trabalhadas = 100
        valor_hora = 5.50
        esperado = 'NUMBER = 25 \nSALARY = U$ 550.00'

        self.assertEqual(calcula_salario(
            funcionario, horas_trabalhadas, valor_hora), esperado)
