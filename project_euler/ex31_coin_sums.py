def main(pence, coins):
    # Dynamic Programming Algorithms
    ways = [0] * (pence + 1)
    ways[0] = 1

    for c in coins:
        for i in range(c, pence + 1):
            ways[i] += ways[i - c]
    return ways[-1]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print(main(200, coins))
