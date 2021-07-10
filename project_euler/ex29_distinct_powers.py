def calc_len(a, b):
    return len(
        {i**j for i in range(a[0], a[1]+1) for j in range(b[0], b[1]+1)}
    )


def main():
    # assert calc_len((2, 5), (2, 5)) == 15
    print(calc_len((2, 100), (2, 100)))


if __name__ == '__main__':
    main()
