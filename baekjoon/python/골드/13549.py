import sys
from collections import deque


def bfs(n, k):
    len_point = 100001
    t = [-1] * len_point
    queue = deque()

    t[n] = 0
    queue.append(n)

    while queue:
        point = queue.popleft()

        if point == k:
            break

        if point * 2 < len_point and t[point * 2] < 0:
            queue.appendleft(point * 2)

            t[point * 2] = t[point]

        for d in [-1, 1]:
            if len_point > point + d >= 0 > t[point + d]:
                queue.append(point + d)

                t[point + d] = t[point] + 1

    return t


if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())

    times = bfs(N, K)

    print(times[K])
