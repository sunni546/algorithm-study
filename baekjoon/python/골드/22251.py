import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K, P, X = map(int, input().split())

    x = list(map(int, f'{X}'))
    if K > len(x):
        x = [0] * (K - len(x)) + x

    change = [(0, 4, 3, 3, 4, 3, 2, 3, 1, 2),
              (4, 0, 5, 3, 2, 5, 6, 1, 5, 4),
              (3, 5, 0, 2, 5, 4, 3, 4, 2, 3),
              (3, 3, 2, 0, 3, 2, 3, 2, 2, 1),
              (4, 2, 5, 3, 0, 3, 4, 3, 3, 2),
              (3, 5, 4, 2, 3, 0, 1, 4, 2, 1),
              (2, 6, 3, 3, 4, 1, 0, 5, 1, 2),
              (3, 1, 4, 2, 3, 4, 5, 0, 4, 3),
              (1, 5, 2, 2, 3, 2, 1, 4, 0, 1),
              (2, 4, 3, 1, 2, 1, 2, 3, 1, 0)]

    case = 0

    for i in range(1, N + 1):
        if i == X:
            continue

        i = list(map(int, f'{i}'))
        if K > len(i):
            i = [0] * (K - len(i)) + i

        p = P
        for j in range(K):
            if x[j] != i[j]:
                p -= change[x[j]][i[j]]

            if p < 0:
                break

        if p >= 0:
            case += 1

    print(case)
