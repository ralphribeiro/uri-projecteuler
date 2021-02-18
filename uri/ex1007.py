def calcula_diferenca(A: int, B: int, C: int, D: int):       
    if (not isinstance(A, int) or
            not isinstance(B, int) or
            not isinstance(C, int) or
            not isinstance(D, int)):
        raise(TypeError)

    D = A * B - C * D
    return f'DIFERENCA = {D}'