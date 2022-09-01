"""
    Pandigital prime


    We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and
is also prime.

    >>> is_pandigital(24413)
    False
    >>> is_pandigital(123456)
    True

    What is the largest n-digit pandigital prime that exists?
"""

from itertools import count, islice, compress
from math import sqrt
from multiprocessing import Pool

from tqdm import tqdm


def is_prime(num):
    return any(
        num % factor
        for factor in range(2, num)
    )


def generate_primes():
    yield 2
    for num in count(3, 2):
        if is_prime(num):
            yield num


def is_pandigital(num):
    list_num = tuple(str(num))
    expected = tuple(str(ln) for ln in range(1, len(list_num) + 1))
    return sorted(list_num) == sorted(expected)


def check_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

    
def gen_primes_range(l, u):
    NBR_PROCESSES = 6
    pool = Pool(processes=NBR_PROCESSES)
    number_range = range(l, u)  # C
    # are_primes = pool.map(check_prime, number_range)  # original
    # primes = np.array(number_range)[np.array(are_primes)]  # original
    are_primes = pool.map(check_prime, number_range)
    return [p for p in compress(number_range, are_primes)]


def main():
    under = 800000000
    upper = 900000000
    my_precious = 0
    primes = gen_primes_range(under, upper)
    for prime in primes:
        if is_pandigital(prime):
            print(prime)
            my_precious = prime

    print(my_precious)
    return my_precious


if __name__ == '__main__':
    main()
