from array import array


def obtem_qtd(k: int, seq: array):
    contador = 0
    while seq:
        for i in range(1, len(seq) + 1):
            if k == sum(seq[:i]):
                contador += 1
        seq.pop(0)
    return contador


SEQ = [2, 0, 1, 1, 0, 0, 8, 4, 1, 3]
N = 10
K = 4

arr = array("b", SEQ)

assert obtem_qtd(K, arr) == 5


N2 = 15
K2 = 0

SEQ2 = [0, 0, 0, 0, 0, 5, 1, 2, 0, 1, 0, 0, 0, 51, 0, 0]

arr2 = array("b", SEQ2)

assert obtem_qtd(K2, arr2) == 25
