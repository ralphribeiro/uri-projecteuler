from unittest import TestCase
from exercicios.ex1024 import criptografa

class TesteEx1024(TestCase):
    # def test_primeira_passada_somente_caracteres_que_sejam_letras_minúsculas_e_maiúsculas_devem_ser_deslocadas_3_posicoes_para_a_direita(self):
    #     chamada = 'a'
    #     esperado = chr(ord(chamada) + 3)

    #     self.assertEqual(criptografa(chamada), esperado)

    # def test_segunda_passada_linha_devera_ser_ivertida(self):
    #     chamada = ('bc')
    #     esperado = 'fe'

    #     self.assertEqual(criptografa(chamada), esperado)

    # def ultima_passada_todo_e_qualquer_caractere_a_partir_da_metade_em_diante_devem_ser_deslocados_uma_posição_para_a_esquerda(self):
    #     chamada = 'paralelepipedo'
    def test_um(self):
        chamada = 'Texto #3'
        esperado = '3# rvzgV'

        self.assertEqual(criptografa(chamada), esperado)

    def test_dois(self):
        chamada = 'abcABC1'
        esperado = '1FECedc'

        self.assertEqual(criptografa(chamada), esperado)

    def test_tres(self):
        chamada = 'vxpdylY .ph'
        esperado = r'ks. \n{frzx'

        self.assertEqual(criptografa(chamada), esperado)

    def test_quatro(self):
        chamada = 'vv.xwfxo.fd'
        esperado = 'gi.r{hyz-xx'

        self.assertEqual(criptografa(chamada), esperado)
    
