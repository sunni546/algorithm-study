import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        n = int(input())

        way = 0

        while n >= 0:
            way += n // 2 + 1

            n -= 3

        print(way)
