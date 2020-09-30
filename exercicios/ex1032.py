from collections import deque


def encontra_sobrevivente(n: int) -> int:
    pessoas = deque()
    [pessoas.append(x+1) for x in range(n)]

    def primo():
        yield 2
        mult = 0
        for n in range(3, 1000):
            for i in range(2, n):
                if n % i == 0:
                    mult += 1
            if mult == 0:
                yield n
            else:
                mult = 0

    p = primo()

    while len(pessoas) > 1:
        pessoas.rotate(-(next(p)-1))
        pessoas.popleft()

    return pessoas.pop()
