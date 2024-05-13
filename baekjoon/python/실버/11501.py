import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        stocks = list(map(int, input().split()))

        revenue = 0
        max_stock = stocks[N - 1]

        for i in range(N - 1, -1, -1):
            if stocks[i] < max_stock:
                revenue += max_stock - stocks[i]

            elif stocks[i] > max_stock:
                max_stock = stocks[i]

        print(revenue)
