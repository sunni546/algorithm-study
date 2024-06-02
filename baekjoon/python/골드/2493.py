import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    heights = list(map(int, input().split()))

    towers = [0] * N

    queue = deque()
    queue.append((N - 1, heights[N - 1]))

    for i in range(N - 2, -1, -1):
        while queue:
            tower = queue.pop()

            if heights[i] >= tower[1]:
                towers[tower[0]] = i + 1

            else:
                queue.append(tower)
                break

        queue.append((i, heights[i]))

    for t in towers:
        print(t, end=' ')
