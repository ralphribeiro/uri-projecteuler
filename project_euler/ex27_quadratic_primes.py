from math import sqrt
from time import perf_counter_ns


def fancy_timer(func):
    def inner(*args):
        init = perf_counter_ns()
        ret = func(*args)
        end = perf_counter_ns()
        print(func.__name__, ' ', (end - init)/10**6, 'ms')
        return ret
    return inner


def eh_primo(n) -> bool:
    if n < 2 or n % 2 == 0:
        return False
    elif n == 2:
        return True
    else:
        for x in range(3, int(sqrt(n) + 1), 2):
            if n % x == 0:
                return False
    return True


@fancy_timer
def calc(a_limite=1000, b_limite=1000):
    maior = [0, 0, 0]
    for a in range((a_limite * -1) + 1, a_limite):
        for b in range(2, b_limite):
            if eh_primo(b):
                cont = 0
                n = 0
                while eh_primo((n ** 2) + (a * n) + b):
                    cont += 1
                    n += 1
                if cont > maior[0]:
                    maior = [cont, a, b]
    return maior[1] * maior[2]


if __name__ == "__main__":
    print(calc(1000, 1000))
