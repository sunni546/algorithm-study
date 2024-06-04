import sys
import heapq


def dijkstra(start, cs):
    c = [INF] * N
    c[start] = 0

    q = []
    heapq.heappush(q, (c[start], start))

    while q:
        cost, barn = heapq.heappop(q)
        if c[barn] < cost:
            continue

        for key, value in cs[barn].items():
            if cost + value < c[key]:
                c[key] = cost + value
                heapq.heappush(q, (c[key], key))

    return c


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())

    INF = float("inf")

    cows = [{} for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int, input().split())

        if B - 1 in cows[A - 1]:
            if cows[A - 1][B - 1] > C:
                cows[A - 1][B - 1] = cows[B - 1][A - 1] = C

        else:
            cows[A - 1][B - 1] = cows[B - 1][A - 1] = C

    costs = dijkstra(0, cows)
    print(costs[N - 1])
