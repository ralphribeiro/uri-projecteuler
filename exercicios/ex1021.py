def calcula_notas_moedas(valor: float):
    moeda = (100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01)    
    
    retorno = ''
    for m in moeda:
        qtd = int(valor // m)
        valor = valor % m
        retorno += f'{m}: {qtd}\n'

    return retorno


print(calcula_notas_moedas(91.01))