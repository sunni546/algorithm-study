import sys
import heapq


def dijkstra(r, start_city):
    min_time = [INF] * N
    min_time[start_city] = 0

    q = []
    heapq.heappush(q, (min_time[start_city], start_city))

    while q:
        time, city = heapq.heappop(q)

        if min_time[city] < time:
            continue

        for c, t in r[city]:
            if time + t < min_time[c]:
                min_time[c] = time + t
                heapq.heappush(q, (min_time[c], c))

    return min_time


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, X = map(int, input().split())

    INF = float("inf")

    roads = [[] for _ in range(N)]
    for _ in range(M):
        start, end, T = map(int, input().split())
        roads[start - 1].append([end - 1, T])

    X -= 1
    times = dijkstra(roads, X)

    for i in range(N):
        if i != X:
            times[i] += dijkstra(roads, i)[X]

    print(max(times))
