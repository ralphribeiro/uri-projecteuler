from collections import deque

letra_numero = {chr(k): v for k, v in enumerate(range(1, 7), start=65)}


class Linha:
    def __init__(self, *args) -> None:
        self.i, self.xa, self.ya, self.xb, self.yb = args
        self.comprimento = self.__calcula_comprimento()

    def __repr__(self) -> str:
        return (f'linha:{self.i}, xa:{self.xa}, ya:{self.ya},'
                f' xb:{self.xb}, yb:{self.yb}')

    def __calcula_comprimento(self):
        return round(((self.xb-self.xa)**2 +
                      (self.yb-self.ya)**2)**(1/2), 2)


class Caso:
    def __init__(self) -> None:
        self.linhas = deque()

    def adiciona_linha(self, arg):
        self.linhas.append(arg)


def converte_pontos(linha_raw):
    a, b = linha_raw.split(' ')
    xa = int(a[1])
    xb = int(b[1])
    ya = int(letra_numero[a[0]])
    yb = int(letra_numero[b[0]])
    return xa, ya, xb, yb


def triagem_casos(arg: str):
    entrada = arg.split('\n')
    entrada.remove('')
    _ = entrada.pop(0)
    casos = []

    while len(entrada) > 0:
        n_linhas = int(entrada.pop(0))
        caso = Caso()

        for _ in range(n_linhas):
            caso.adiciona_linha(converte_pontos(entrada.pop(0)))
        casos.append(caso)

    return casos


def main(arg: str):
    casos = triagem_casos(arg)

    for c in casos:
        
