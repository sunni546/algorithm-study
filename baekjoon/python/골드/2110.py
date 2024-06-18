import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, C = map(int, input().split())

    x = []
    for _ in range(N):
        x.append(int(input()))
    x.sort()

    dist = 0

    min_dist = 1
    max_dist = x[-1] - x[0]

    while min_dist <= max_dist:
        mid_dist = (min_dist + max_dist) // 2

        c = 1
        prev = 0

        for i in range(N):
            if x[i] - x[prev] >= mid_dist:
                c += 1
                prev = i

        if c >= C:
            dist = mid_dist
            min_dist = mid_dist + 1
        else:
            max_dist = mid_dist - 1

    print(dist)
