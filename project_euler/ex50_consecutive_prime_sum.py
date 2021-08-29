""" 
    The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
from math import sqrt


def gen_primes(limit):
    D = {}
    q = 2
    ret = []
    while q < limit:
        if q not in D:
            ret.append(q)
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
    return ret


def is_prime(n):
    if n < 2:
        return False
    sqrt_number = sqrt(n)
    for i in range(2, int(sqrt_number) + 1):
        if (n / i).is_integer():
            return False
    return True


def calc(limit):
    primes = gen_primes(limit)
    len_p = len(primes)
    g = 0
    len_ = 0
    for i in range(len_p):
        for j in range(i + len_, len_p):
            sum_ = sum(primes[i:j])
            if sum_ >= limit:
                break
            if is_prime(sum_):
                len_ = j - i
                g = sum_
    return g


def main():
    assert calc(100) == 41
    assert calc(1000) == 953
    print(calc(1_000_000))


if __name__ == '__main__':
    main()
