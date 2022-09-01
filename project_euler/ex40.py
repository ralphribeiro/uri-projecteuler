"""
Champernowne's constant



An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

"""

def dth(num) -> int:
    raw = ''.join(str(n) for n in range(1, num+1))
    ret = int(raw[num-1])
    print(ret)
    return ret


def main(range_):
    n = 1
    ret = 1
    for _ in range(range_):
        n *= 10
        ret *= dth(n)
    return ret
