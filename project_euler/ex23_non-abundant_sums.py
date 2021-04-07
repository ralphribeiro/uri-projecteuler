"""
    A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

from functools import lru_cache

min_num = 24
max_num = 28123


def divisors(n):
    return [d for d in range(1, n) if not n % d]


def abundant_number(n):
    if sum(divisors(n)) > n:
        return divisors


def main():
    abundant_numbers = [n for n in range(
        min_num, max_num+1) if abundant_number(n)]


# for i in range(min_num, max_num+1):
    # for j in range(min_num, max_num+1):
    # if abundant_numbers[i]
main()
