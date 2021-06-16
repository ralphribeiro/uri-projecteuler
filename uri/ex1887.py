""" 
N - número de cidades
M - número de vias iniciais
Q - número de vias que serão adicionadas com o tempo

VIA (a, b, c)
a e b - cidades ligadas por esta via
c - custo de manutenção
 """

N, M, Q = 4, 3, 5
VIAS = (
    (1, 2, 5),
    (2, 3, 6),
    (3, 4, 7),
    (1, 4, 8),
    (1, 2, 4),
    (2, 4, 5),
    (3, 4, 5),
    (1, 4, 6)
)


def calcula_custo(n, m, q, vias):
    retorno = []
    custo = 0
    for i, v in enumerate(vias, start=1):
        a, b, c = v
        custo += c
        if i == m:
            retorno.append(custo)
    return retorno


c = calcula_custo(N, M, Q, VIAS)
print(c)
