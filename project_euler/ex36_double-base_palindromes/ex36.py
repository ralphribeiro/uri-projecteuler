def is_palindrome(number):
    n = str(number)
    if n.startswith('0'):
        return False
    return str(number) == str(number)[::-1]


def to_binary(number):
    return bin(number).replace('0b', '')


def main(number):
    palindromes = []
    for n in range(1, number + 1):
        if is_palindrome(n):
            binary = to_binary(n)
            if is_palindrome(binary):
                palindromes.append(n)
    return sum(palindromes)


r = main(10**6)
print(r)
