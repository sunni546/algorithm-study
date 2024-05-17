import sys
from collections import deque


def bfs(g, t, d):
    visited = [[False] * m for _ in range(n)]
    visited[t[0]][t[1]] = True

    queue = deque()
    queue.append(t)

    while queue:
        t = queue.popleft()

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vx, vy = t[0] + x, t[1] + y

            if 0 <= vx < n and 0 <= vy < m:
                if not visited[vx][vy]:
                    if g[vx][vy] == 0:
                        d[vx][vy] = 0
                        visited[vx][vy] = True
                    else:
                        queue.append((vx, vy))
                        d[vx][vy] = d[t[0]][t[1]] + 1
                        visited[vx][vy] = True


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())

    graph = []
    target = None
    distances = [[-1] * m for _ in range(n)]

    for i in range(n):
        g = list(map(int, input().split()))
        graph.append(g)

        if 2 in g:
            target = (i, g.index(2))

    distances[target[0]][target[1]] = 0
    bfs(graph, target, distances)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                print(distances[i][j], end=' ')
            else:
                print(0, end=' ')
        print()
