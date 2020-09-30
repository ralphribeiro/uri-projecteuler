def calcula_numero_de_cedulas(valor: int):
    notas = (100, 50, 20, 10, 5, 2, 1)
    retorno = f'{valor}\n'
    for n in notas:
        qtd_notas = 0
        for i in range(valor // n):
            qtd_notas += 1
            valor -= n
        retorno += f'{qtd_notas} nota(s) de R$ {n:.2f}\n'

    return retorno.replace('.', ',')
