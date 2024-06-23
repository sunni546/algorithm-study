import sys
from collections import deque


def bfs_fire(m, f):
    visited = [[-1 for _ in range(C)] for _ in range(R)]

    queue = deque(f)

    for i, j in f:
        visited[i][j] = 0

    while queue:
        f = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = f[0] + dx, f[1] + dy

            if 0 <= x < R and 0 <= y < C and m[x][y] != '#':
                if visited[x][y] < 0:
                    visited[x][y] = visited[f[0]][f[1]] + 1
                    queue.append((x, y))

    return visited


def bfs(m, v_f, j):
    visited = [[-1 for _ in range(C)] for _ in range(R)]

    queue = deque([j])
    visited[j[0]][j[1]] = 0

    while queue:
        j = queue.popleft()

        if j[0] == 0 or j[0] == R - 1 or j[1] == 0 or j[1] == C - 1:
            return visited[j[0]][j[1]] + 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = j[0] + dx, j[1] + dy

            if 0 <= x < R and 0 <= y < C and m[x][y] == '.':
                if visited[x][y] < 0 and v_f[x][y] > visited[j[0]][j[1]] + 1:
                    visited[x][y] = visited[j[0]][j[1]] + 1
                    queue.append((x, y))

    return 0


if __name__ == '__main__':
    input = sys.stdin.readline
    R, C = map(int, input().split())

    maze, jihoon, fire = [], (), []
    
    for r in range(R):
        row = list(input().rstrip())

        for c in range(C):
            if row[c] == 'J':
                jihoon = (r, c)
            elif row[c] == 'F':
                fire.append((r, c))

        maze.append(row)

    if fire:
        visited_fire = bfs_fire(maze, fire)
    else:
        visited_fire = [[10000 for _ in range(C)] for _ in range(R)]
    min_time = bfs(maze, visited_fire, jihoon)

    if min_time:
        print(min_time)
    else:
        print('IMPOSSIBLE')
