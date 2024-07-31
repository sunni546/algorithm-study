import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())

    jewel = [list(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]

    jewel.sort()
    bags.sort()

    max_total = 0
    j = []

    for bag in bags:
        while jewel and jewel[0][0] <= bag:
            heapq.heappush(j, -jewel[0][1])
            heapq.heappop(jewel)
        if j:
            max_total += -heapq.heappop(j)

    print(max_total)

