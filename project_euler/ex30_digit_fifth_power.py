def main(n):
    """Calculates the sum of all numbers that can be written as the sum of
    the <n> powers of their digits.

    Args:
        n (int): nth power
    """
    pv = {v: v**n for v in range(10)}
    match = []
    for num in range(2**n, 10**(n+1)):
        digits = (int(dg) for dg in str(num))
        sum_ = sum(pv[d] for d in digits)
        if num == sum_:
            match.append(num)
    return sum(match)


assert main(4) == 19316


if __name__ == '__main__':
    print(main(5))
