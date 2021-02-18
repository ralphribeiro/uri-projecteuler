from math import sqrt

def calcula_distancia_entre_dois_pontos(A: float, B: float) -> str:
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]

    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return f'{dist:.4f}'
