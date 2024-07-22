import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # numbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
    INF = float('inf')

    minDP = [INF for _ in range(101)]

    T = int(input())

    minDP[2:8] = [1, 7, 4, 2, 6, 8]
    for i in range(8, 101):
        for j in range(2, i - 1):
            minDP[i] = min(minDP[i], int(str(minDP[j]) + str(minDP[i-j])))

            if j == 6:
                minDP[i] = min(minDP[i], minDP[i - j] * 10)

    for _ in range(T):
        n = int(input())

        min_number = minDP[n]
        max_number = 0

        if n % 2 == 1:
            max_number = 7
            n -= 3

        while n > 1:
            max_number = max_number * 10 + 1
            n -= 2

        print(min_number, max_number)
    