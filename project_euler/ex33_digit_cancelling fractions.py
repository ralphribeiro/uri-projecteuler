def convert_fraction(num, den):
    d = [int(n) for n in str(den)]
    n = [int(n) for n in str(num)]
    com = [i for i in n if i in d]
    if len(com) > 0:
        c = com.pop()
        if c > 0:
            n.remove(c)
            d.remove(c)
            return n.pop(), d.pop()
    return 0, 0


def main():
    ret = 1
    for i in range(10, 100):
        for j in range(10, 100):
            if i < j:
                r = i / j
                n, d = convert_fraction(i, j)
                if d > 0 and r == n / d:
                    ret *= d/n
                    print(f'{i}/{j}, {n}/{d}')
    print(int(ret))


main()
