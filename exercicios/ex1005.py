def calcula_media(A: float, B: float):
    if (not isinstance(A,float) or not isinstance(B, float)):
        raise TypeError

    M = (A * 3.5 + B * 7.5) / 11
    return f'MEDIA = {M:.5f}'
