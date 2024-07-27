import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    mars = []

    for _ in range(N):
        mars.append(list(map(int, input().split())))

    for j in range(1, M):
        mars[0][j] += mars[0][j - 1]

    for i in range(1, N):
        go_right = mars[i][:]
        go_left = mars[i][:]

        go_right[0] += mars[i - 1][0]
        for j in range(1, M):
            go_right[j] += max(mars[i - 1][j], go_right[j - 1])

        go_left[M - 1] += mars[i - 1][M - 1]
        for j in range(M - 2, -1, -1):
            go_left[j] += max(mars[i - 1][j], go_left[j + 1])

        for j in range(M):
            mars[i][j] = max(go_right[j], go_left[j])

    print(mars[N - 1][M - 1])
