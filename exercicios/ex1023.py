import os
from itertools import count


class Casa():
    def __init__(self, numero_moradores, consumo, consumo_por_pessoa):
        self.numero_moradores = numero_moradores
        self.consumo = consumo
        self.consumo_por_pessoa = consumo_por_pessoa


class Cidade():
    def __init__(self, n):
        self.nome = f'C#{n}'
        self.casas = []
        self.consumo_medio = 0

    def insere_casa(self, casa):
        self.casas.append(casa)

    
def calcula_estiagem(path: str) -> list:
    contador_cidade = count(start=1)
    if not path.lower().endswith('.txt'):
        return 'arquivo inválido'
    if not path in os.listdir('.'):
        return 'arquivo inexistente'

    with open(path, 'r') as arquivo:
        linhas = arquivo.read()

    lista_entrada = linhas.split('\n')

    cidades = []
    for l in lista_entrada:
        if l == '0':
            ...
        elif l.isnumeric():
            cidades.append(Cidade(len(cidades) + 1))
        else:
            qtd_moradores, consumo_total = l.split(' ')
            qtd_moradores = int(qtd_moradores)
            consumo_total = int(consumo_total)
            consumo_individual = int(consumo_total / qtd_moradores)
            cas = Casa(qtd_moradores, consumo_total, consumo_individual)
            cid = cidades[len(cidades) - 1]
            cid.casas.append(cas)
            cidades[len(cidades) - 1] = cid

    retorno = ''
    c_medio = 0
    for cid in cidades:
        retorno += f'{cid.nome}\n'
        for casa in cid.casas:
            retorno += f'{casa.numero_moradores} - {casa.consumo_por_pessoa}\n'
            c_medio += casa.consumo_por_pessoa

        c_medio = c_medio / len(cid.casas)
        retorno += f'Consumo médio - {c_medio:.1f} m3\n'

    return retorno


path = 'ex1023.txt'

print(calcula_estiagem(path))
