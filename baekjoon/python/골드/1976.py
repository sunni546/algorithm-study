import sys
from collections import deque


def check_cities(c, start, end):
    can_go = False
    visited = [False] * N

    queue = deque()
    queue.append(start)

    while queue:
        city = queue.popleft()
        visited[city] = True

        if city == end:
            can_go = True
            break

        for i in range(N):
            if c[city][i] and not visited[i]:
                if not c[start][i]:
                    c[start][i] = 1
                if not c[i][start]:
                    c[i][start] = 1

                queue.append(i)

    return can_go


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    cities = []
    for _ in range(N):
        cities.append(list(map(int, input().split())))

    travel_plan = list(map(int, input().split()))

    now = travel_plan[0] - 1
    can_travel = True

    for i in range(1, M):
        next_city = travel_plan[i] - 1

        if not check_cities(cities, now, next_city):
            can_travel = False
            break

        now = next_city

    if can_travel:
        print('YES')
    else:
        print('NO')
