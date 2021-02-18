def calcula_area_circunferencia(raio: float):
    if (not isinstance(raio, float)):
        raise TypeError
    elif (raio < 0):
        return 0

    pi = 3.14159
    A = pi * raio**2
    return f'A = {A:.4f}'
