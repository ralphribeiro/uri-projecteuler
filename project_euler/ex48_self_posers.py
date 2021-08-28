""" 
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""


def self_powers(num):
    return sum(n**n for n in range(1, num+1))


# assert self_powers(10) == 10405071317


def main():
    ret = str(self_powers(1000))
    print(ret[-10:])

if __name__ == '__main__':
    main()