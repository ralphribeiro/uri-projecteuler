def calcula_total(linha_um: str, linha_dois: str):
    q1, v1 = converte_valor(linha_um)
    q2, v2 = converte_valor(linha_dois)
    return f'VALOR A PAGAR: R$ {q1*v1 + q2*v2:.2f}'


def converte_valor(valor):
    _, qtd, vl = valor.split(' ')
    return int(qtd), float(vl)