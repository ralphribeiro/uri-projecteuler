def calcula_produto(A: int, B: int):
    if (not isinstance(A, int) or not isinstance(B, int)):
        raise TypeError

    P = A * B
    return f'PROD = {P}'