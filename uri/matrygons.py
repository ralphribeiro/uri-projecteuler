""" 
    Dado um número total fixo de lados N, calcule o maior número de polígonos
que podem fazer parte de um matrygon de modo que o número total de lados entre
todos os polígonos nele seja exatamente N.
"""
from itertools import accumulate
from operator import mul


def calc_poligonos(total_vs):
    vertices = []
    while total_vs:
        if total_vs % 2 == 0:
            total_vs /= 2
            vertices.append(total_vs)
        if total_vs % 3 == 0:
            total_vs /= 3
            vertices.append(total_vs)
        else:
            break
    return len(vertices)

assert calc_poligonos(22) == 1
assert calc_poligonos(24) == 3

def main():
    max = [0, 0]
    for i in range(3, 10**6):
        qtd_vs = calc_poligonos(i)
        if qtd_vs > max[0]:
            max[0] = qtd_vs
            max[1] = i
            
    print(max)

main()