import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, a, b = map(int, input().split())

    if a + b > N + 1:
        print(-1)

    else:
        if a >= b:
            buildings = [i + 1 for i in range(a)] + [b - i - 1 for i in range(b - 1)]
        else:
            buildings = [i + 1 for i in range(a - 1)] + [b - i for i in range(b)]

        if len(buildings) < N:
            buildings = [buildings[0]] + [1 for _ in range(N - len(buildings))] + buildings[1:]

        for building in buildings:
            print(building, end=' ')
