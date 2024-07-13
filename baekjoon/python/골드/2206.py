import sys
from collections import deque


def bfs(g, n, m):
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    queue = deque()
    queue.append((0, 0, False))

    while queue:
        i, j, is_break = queue.popleft()

        if i == n - 1 and j == m - 1:
            return visited[n - 1][m - 1][is_break]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i + dx, j + dy

            if 0 <= x < n and 0 <= y < m:
                if not g[x][y] and not visited[x][y][is_break]:
                    visited[x][y][is_break] = visited[i][j][is_break] + 1
                    queue.append((x, y, is_break))

                elif g[x][y] and not is_break:
                    visited[x][y][not is_break] = visited[i][j][is_break] + 1
                    queue.append((x, y, not is_break))

    return -1


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())

    graph = [list(map(int, input().rstrip())) for _ in range(N)]

    print(bfs(graph, N, M))
