from collections import deque
from typing import List, Tuple


def calcula_suicidio(caso: List[Tuple]) -> str:
    retorno: str = str()
    for i, entradas in enumerate(caso, start=1):
        n, k = entradas
        if not 1 <= n <= 10000 or not 1 <= k <= 1000:
            retorno += f'Case {i}: entrada inválida\n'
        else:
            lista_individuos: deque = deque()
            [lista_individuos.append(x+1) for x in range(n)]

            while len(lista_individuos) > 1:
                lista_individuos.rotate(-(k-1))
                lista_individuos.popleft()

            retorno += f'Case {i}: {lista_individuos.pop()}\n'

    return retorno
