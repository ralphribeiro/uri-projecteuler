"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from itertools import accumulate
from math import factorial
from operator import add


fact_str = str(factorial(100))

fact_digits = [int(d) for d in fact_str if int(d) > 0]

r = max(accumulate(fact_digits, add))

print(r)