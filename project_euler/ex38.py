"""
Pandigital multiples
"""

def concatenated_product(number, multiples):
    return ''.join(str(m * number) for m in range(1, multiples + 1))

def run():
    higher = 0
    for n in range(1, 100000001):
        for m in range(1, 101):
            ret = concatenated_product(n, m)
            if len(ret) == 9 and int(ret) > higher:
                higher = int(ret)
                print(n, m, higher)


run()
