""" 
    A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be, seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
 """

from collections import Counter


def obtem_tamanho_casas_decimais(num):
    return str(num).split('.')[1]


assert obtem_tamanho_casas_decimais(1/2) == '5'


def obtem_numero_mais_frequente(num):
    algs = list(iter(num))
    seq = algs.pop(0)
    Counter(num)
    while algs:
        if seq in num:
            print('seq: ', seq)
        seq += algs.pop(0)
        


obtem_numero_mais_frequente('1213123123123')
