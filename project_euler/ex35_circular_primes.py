from collections import deque
import math


def is_prime(n):
    sqrt_number = math.sqrt(n)
    for i in range(2, int(sqrt_number) + 1):
        if (n / i).is_integer():
            return False
    return True


def circular_prime(n):
    if is_prime(n):
        digits = deque(i for i in str(n))
        for _ in range(len(digits)):
            digits.rotate()
            num = int(''.join(n for n in digits))
            if not is_prime(num):
                return False
        return True
    return False


def main(n):
    print(len([i for i in range(2, n+1) if circular_prime(i)]))


main(1000000)
