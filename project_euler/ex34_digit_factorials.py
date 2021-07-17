from math import factorial


def calc_digit_factorial(n):
    return sum(factorial(int(i)) for i in str(n))


def main():
    print(sum(i for i in range(3, 10**5) if calc_digit_factorial(i) == i))


main()
