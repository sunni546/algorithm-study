import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = deque(list(map(int, input().split())))

    robot = deque([False] * N)
    level, k = 0, 0

    while k < K:
        A.rotate(1)
        robot.rotate(1)

        for i in range(N - 1, -1, -1):
            if i == N - 1 and robot[i]:
                robot[i] = False

            if robot[i] and not robot[i + 1] and A[i + 1] >= 1:
                robot[i], robot[i + 1] = robot[i + 1], robot[i]
                if i + 1 == N - 1:
                    robot[i + 1] = False

                A[i + 1] -= 1
                if not A[i + 1]:
                    k += 1

        if A[0] > 0:
            robot[0] = True

            A[0] -= 1
            if not A[0]:
                k += 1

        level += 1

    print(level)
