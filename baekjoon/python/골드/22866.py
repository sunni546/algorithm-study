import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    heights = list(map(int, input().split()))

    visible_buildings = [[0, -1] for _ in range(N)]

    b = []

    for i in range(N):
        while b and heights[b[-1]] <= heights[i]:
            b.pop()

        if b:
            visible_buildings[i][0] = len(b)
            visible_buildings[i][1] = b[-1]

        b.append(i)

    b = []

    for i in range(N - 1, -1, -1):
        while b and heights[b[-1]] <= heights[i]:
            b.pop()

        if b:
            visible_buildings[i][0] += len(b)

            if visible_buildings[i][1] < 0 or i - visible_buildings[i][1] > b[-1] - i:
                visible_buildings[i][1] = b[-1]

        b.append(i)

    for v in visible_buildings:
        if v[0]:
            print(v[0], v[1] + 1)

        else:
            print(v[0])
