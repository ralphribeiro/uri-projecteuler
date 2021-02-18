def calcula_media(A: float, B: float, C: float):
    if (not isinstance(A, float) or
            not isinstance(B, float) or
            not isinstance(C, float)):
        raise TypeError

    M = (2 * A + 3 * B + 5 * C) / 10
    return f'MEDIA = {M}'
