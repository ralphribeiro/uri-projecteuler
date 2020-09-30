def calcula_idade_em_dias(dias: int):
    ano = dias // 365
    mes = (dias % 365) // 30
    dia = (dias % 365) % 30
    return f'{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)'
