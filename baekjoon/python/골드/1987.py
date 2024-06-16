import sys


def move(v, i, j, m):
    alphabet = road[i][j]
    v[ord(alphabet) - 65] = True

    for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x, y = i + di, j + dj

        if 0 <= x < R and 0 <= y < C and not v[ord(road[x][y]) - 65]:
            m = move(v, x, y, m)

            v[ord(road[x][y]) - 65] = False

    return max(m, v.count(True))


if __name__ == '__main__':
    input = sys.stdin.readline
    R, C = map(int, input().split())

    road = []

    for _ in range(R):
        road.append(list(input().rstrip()))

    visited = [False] * 26

    max_move = move(visited, 0, 0, 0)
    print(max_move)
