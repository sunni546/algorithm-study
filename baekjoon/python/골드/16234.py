import sys
from collections import deque


def make_union(v, country):
    union = deque([country])
    people = A[country[0]][country[1]]

    queue = deque([country])
    v[country[0]][country[1]] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not v[nx][ny] and L <= abs(A[nx][ny] - A[x][y]) <= R:
                    queue.append((nx, ny))
                    v[nx][ny] = True

                    union.append((nx, ny))
                    people += A[nx][ny]

    if len(union) == 1:
        return False
    else:
        people //= len(union)
        while union:
            x, y = union.popleft()
            A[x][y] = people

        return True


if __name__ == '__main__':
    input = sys.stdin.readline
    N, L, R = map(int, input().split())

    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    is_moved = True
    day = 0

    while is_moved:
        is_moved = False
        visited = [[False for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    if make_union(visited, (i, j)):
                        is_moved = True

        if is_moved:
            day += 1

    print(day)
