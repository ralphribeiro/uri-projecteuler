"""
    Pandigital multiples

    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 x 1 = 192
        192 x 2 = 384
        192 x 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)
        >>> concatenated_product(192, 3)
        192384576

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product of
9 and (1,2,3,4,5).
        >>> concatenated_product(9, 5)
        918273645

    Check if number is pandigital:
        >>> is_pandigital(918273645)
        True
        >>> is_pandigital(999999999)
        False
    
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(number):
    num_digits = str(number)
    return len(num_digits) == 9 and set(num_digits) == set('123456789')


def proc(start, end):
    greater = 0
    for n in range(start, end):
        for r in range(1, 9):
            prod = concatenated_product(n, r)
            if is_pandigital(prod):
                greater = n
    return greater


def main():
    candidates = []
    for base_num in range(9999, 4999, -1):
        candidate = 100002 * base_num
        if is_pandigital(candidate):
            candidates.append(candidate)

    for base_num in range(333, 99, -1):
        candidate = 1002003 * base_num
        if is_pandigital(candidate):
            candidates.append(candidate)

    return max(candidates)


if __name__ == '__main__':
    print(main())
