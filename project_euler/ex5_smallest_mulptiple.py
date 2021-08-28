"""
Smallest multiple.

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
"""

from datetime import datetime


def time_delta(func):
    def inner(*args):
        t_init = datetime.now()
        ret = func(*args)
        t_final = datetime.now() - t_init
        print(f'{t_final.seconds}s | {t_final.microseconds}us')
        return ret
    return inner


def gcd(x: int, y: int) -> int:
    """ Greatest Common Divisor. """
    return x if y == 0 else gcd(y, x % y)


def lcm(x: int, y: int) -> int:
    """ Least Common Multiple. """
    return (x * y) // gcd(x, y)


def check_mul(divds: list, b: int):
    for d in divds:
        if b % d != 0:
            return False
    return True


@time_delta
def calc_min_multiple(ni, ne):
    g = ni
    for i in range(ni, ne + 1):
        g = lcm(g, i)
    return g


def main():
    print(calc_min_multiple(1, 10))
    print(calc_min_multiple(1, 20))


if __name__ == '__main__':
    main()
