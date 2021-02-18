def calcula_soma(A: int, B: int):
    if (not isinstance(A, int) or not isinstance(B, int)):
        raise TypeError
    
    return f'X = {A + B}'

