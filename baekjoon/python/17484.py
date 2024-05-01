import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())

    spaces = []
    for _ in range(n):
        spaces.append(list(map(int, input().split())))

    MAX_PRICE = 601
    prices = [[[MAX_PRICE, MAX_PRICE, MAX_PRICE] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0:
                prices[i][j] = [spaces[i][j] for _ in range(3)]

            else:
                if 0 < j:
                    prices[i][j][0] = min(prices[i - 1][j - 1][1], prices[i - 1][j - 1][2]) + spaces[i][j]

                prices[i][j][1] = min(prices[i - 1][j][0], prices[i - 1][j][2]) + spaces[i][j]

                if j < m - 1:
                    prices[i][j][2] = min(prices[i - 1][j + 1][0], prices[i - 1][j + 1][1]) + spaces[i][j]

    min_value = MAX_PRICE
    for price in prices[n - 1]:
        min_value = min(min_value, min(price))
    print(min_value)
