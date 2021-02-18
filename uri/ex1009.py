def calcula_salario_com_bonus(nome: str,
                              salario_fixo: float,
                              montante_vendas: float
                              ):
    salario = salario_fixo + 0.15 * montante_vendas
    return f'TOTAL = R$ {salario:.2f}'
