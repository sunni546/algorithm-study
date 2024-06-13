import sys
import heapq


def dijkstra(n, start, tr):
    lr = [[INF for _ in range(n)] for _ in range(n)]

    i, j = start[0], start[1]
    lr[i][j] = tr[i][j]

    q = []
    heapq.heappush(q, (lr[start[0]][start[1]], start))

    while q:
        rupee, location = heapq.heappop(q)
        i, j = location[0], location[1]

        if lr[i][j] < rupee:
            continue

        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ti, tj = i + di, j + dj

            if 0 <= ti < n and 0 <= tj < n:
                if rupee + tr[ti][tj] < lr[ti][tj]:
                    lr[ti][tj] = rupee + tr[ti][tj]
                    heapq.heappush(q, (lr[ti][tj], (ti, tj)))

            else:
                continue

    return lr


if __name__ == '__main__':
    input = sys.stdin.readline

    INF = float("inf")
    test = 1

    while True:
        N = int(input())
        if N == 0:
            break

        thief_rupee = []
        for _ in range(N):
            thief_rupee.append(list(map(int, input().split())))

        lost_rupee = dijkstra(N, (0, 0), thief_rupee)

        print(f'Problem {test}: {lost_rupee[N - 1][N - 1]}')

        test += 1
