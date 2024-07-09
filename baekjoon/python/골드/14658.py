import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, L, K = map(int, input().split())

    stars = []

    for _ in range(K):
        x, y = map(int, input().split())
        stars.append((x, y))

    max_star = 1

    for i in range(K):
        for j in range(i + 1, K):
            s = 0

            x, y = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])

            for sx, sy in stars:
                if x <= sx <= x + L and y <= sy <= y + L:
                    s += 1

            max_star = max(max_star, s)

    print(K - max_star)
