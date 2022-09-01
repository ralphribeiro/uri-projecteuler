"""
    Coded triangle numbers

    

    The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    >>> [get_nth_term(t) for t in range(1, 11)]
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

    By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.
    >>> calc_word('SKY')
    55

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?

"""
from string import ascii_uppercase


def get_nth_term(nth: int) -> int:
    return int(nth * (nth + 1) / 2)


def calc_word(word: str) -> int:
    reference = {k: v for v, k in enumerate(ascii_uppercase, 1)}
    return sum(reference[l] for l in word)


NS = [get_nth_term(n) for n in range(1, 21)]


def main():
    count = 0
    with open('words.txt', 'r') as file:
        for word in file.read().split(','):
            word = word.replace('"', '')
            cw = calc_word(word)
            if cw in NS:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
