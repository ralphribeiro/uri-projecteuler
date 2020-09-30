
def calcula_area(linha: str):
    lista = linha.split(' ')
    lista_float = [float(x) for x in lista]
    A = lista_float[0]
    B = lista_float[1]
    C = lista_float[2]

    pi = 3.14159

    area_triangulo = A * C / 2
    area_circulo = pi * C**2
    area_trapezio = C * (A + B) / 2
    area_quadrado = B**2
    area_retangulo = A * B

    r = f'TRIANGULO: {area_triangulo:.3f}'
    r += f'\nCIRCULO: {area_circulo:.3f}'
    r += f'\nTRAPEZIO: {area_trapezio:.3f}'
    r += f'\nQUADRADO: {area_quadrado:.3f}'
    r += f'\nRETANGULO: {area_retangulo:.3f}'
    
    return r