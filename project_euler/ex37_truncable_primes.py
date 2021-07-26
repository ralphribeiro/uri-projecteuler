from math import sqrt


def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def is_prime(n):
    if n < 2:
        return False
    sqrt_number = sqrt(n)
    for i in range(2, int(sqrt_number) + 1):
        if (n / i).is_integer():
            return False
    return True


def truncable_prime(n):
    digits = [s for s in str(n)]
    while len(digits) > 1:
        digits.pop(0)
        d = int(''.join(d for d in digits))
        if not is_prime(d):
            return False

    digits = [s for s in str(n)]
    while len(digits) > 1:
        digits.pop(-1)
        d = int(''.join(d for d in digits))
        if not is_prime(d):
            return False

    return True


def main():
    nums = []
    primes = gen_primes()
    while len(nums) < 11:
        p = next(primes)
        if p > 7 and truncable_prime(p):
            nums.append(p)
    print(sum(nums))


main()
