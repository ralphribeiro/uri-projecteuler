from math import log
from time import perf_counter_ns
from itertools import takewhile



def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    else:
        return True

def miller_rabin(n):
    if not n > 1:
        return False
    for all_ in range(2, min(n-2), int(2*(log(n))**2)):
        x = 


if __name__ == "__main__":
    inicio = perf_counter_ns()
    euler = [n ** 2 + n + 41 for n in range(0, 40)]
    print(len(euler))
    f = list(takewhile(is_prime, euler))
    assert euler == f

    incredible = [n ** 2 - 79 * n + 1601 for n in range(0, 80)]
    print(len(incredible))
    g = list(takewhile(is_prime, incredible))
    assert incredible == g

    for i in range(1000000):
        is_prime(i)

    fim = perf_counter_ns() - inicio
    print('tempo: ', fim / 10**9, ' s')
