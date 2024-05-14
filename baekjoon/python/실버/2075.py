import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    pq = []

    for _ in range(N):
        nums = list(map(int, input().split()))

        for num in nums:
            if len(pq) == N:
                heapq.heappush(pq, max(heapq.heappop(pq), num))
            else:
                heapq.heappush(pq, num)

    print(heapq.heappop(pq))
