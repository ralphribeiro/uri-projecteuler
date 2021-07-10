
# brute force
def coord(n):
    i = j = n // 2
    p = 1
    yield (i, j), p
    count = 1
    add = True
    line = False
    while count <= n:
        for c in range(count*2):
            line = c >= count

            if add:
                if line:
                    i += 1
                else:
                    j += 1
            else:
                if line:
                    i -= 1
                else:
                    j -= 1

            if p < n**2:
                p += 1
            else:
                break

            yield (i, j), p
        add = not add
        count += 1


t = [
    ((2, 2), 1),
    ((2, 3), 2),
    ((3, 3), 3),
    ((3, 2), 4),
    ((3, 1), 5),
    ((2, 1), 6),
    ((1, 1), 7),
    ((1, 2), 8),
    ((1, 3), 9),
    ((1, 4), 10),
    ((2, 4), 11),
    ((3, 4), 12),
    ((4, 4), 13),
    ((4, 3), 14),
    ((4, 2), 15),
    ((4, 1), 16),
    ((4, 0), 17),
    ((3, 0), 18),
    ((2, 0), 19),
    ((1, 0), 20),
    ((0, 0), 21),
    ((0, 1), 22),
    ((0, 2), 23),
    ((0, 3), 24),
    ((0, 4), 25)
]

# assert list(coord(5)) == t


def diags_calc(n: int):
    c = coord(n)
    d = {k: v for k, v in c}
    diag1 = sum(d[i, i] for i in range(n))
    diag2 = sum(d[i, n-1-i] for i in range(n))
    return diag1 + diag2 - 1


# c = coord(5)
# assert diags_calc(5)

def coord2(l_):
    n = (l_-1) // 2
    return (16*n**3 + 30*n**2 + 26*n + 3) // 3


def main():
    # for i in range(5, 20):
    #     if not i % 2 == 0:
    #         print(i, diags_calc(i))
    print(diags_calc(1001))
    print(coord2(1001))


if __name__ == '__main__':
    main()
