def calcula_gasto_cobustivel(H: int, V: int):
    consumo = 12 #Km/l
    distancia = V * H
    gasto = distancia / consumo

    return f'{gasto:.3f}'


assert calcula_gasto_cobustivel(10, 85) == '70.833'
assert calcula_gasto_cobustivel(2, 92) == '15.333'
assert calcula_gasto_cobustivel(22, 67) == '122.833'