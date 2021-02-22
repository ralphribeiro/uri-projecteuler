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


def check_mul(divds: list, b: int):
    for d in divds:
        if b % d != 0:
            return False
    return True


@time_delta
def calc_min_multiple(ni, ne):
    dividers = list(range(ni, ne))
    base_nums = ni

    while True:
        if check_mul(dividers, base_nums):
            return print(base_nums)
        base_nums += 1


calc_min_multiple(1, 10)
calc_min_multiple(1, 20)
