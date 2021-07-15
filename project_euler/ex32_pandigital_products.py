from itertools import permutations

DIGITS = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def main():
    i = 1
    r = set()
    while i <= 2:
        for c in permutations(DIGITS):
            m1 = int(''.join(str(n) for n in c[:i]))
            m2 = int(''.join(str(n) for n in c[i:5]))
            p = int(''.join(str(n) for n in c[5:]))
            if m1 * m2 == p:
                r.add(p)
        i += 1
    return sum(r)

print(main())