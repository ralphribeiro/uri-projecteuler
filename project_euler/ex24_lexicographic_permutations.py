"""
    A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2,
    3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations
from typing import Iterator


def permuta(value: tuple) -> tuple:
    return tuple(permutations(value))


test = (0, 1, 2)
assert permuta(test) == (
    (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)
)


digits = tuple(range(9+1))

result = permuta(digits)

millionth = result[10**6 - 1]

r = str()
for n in millionth:
    r += str(n)

print(r)
