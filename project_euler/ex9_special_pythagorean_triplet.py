"""
Special Pythagorean triplet.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from datetime import datetime
from functools import wraps


def time_delta(func):
    wraps(func)
    def inner(*args):
        t_init = datetime.now()
        ret = func(*args)
        t_final = datetime.now() - t_init
        print(f'{t_final.seconds}s | {t_final.microseconds}us')
        return ret
    return inner


def gen_num():
    n = 1
    while True:
        yield n
        n += 1


@time_delta
def pythagorean_triplet(r):
    for b in gen_num():
        for a in range(1, b):
            c = (a**2 + b**2)**(1/2)
            if c % 1 == 0:
                if (a+b+int(c)) == r:
                    return a, b, int(c)


a, b, c = pythagorean_triplet(1000)

res = a * b * c

print(res)