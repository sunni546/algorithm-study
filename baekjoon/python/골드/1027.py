import sys


def cal_inclination(x, y):
    return (y[1] - x[1]) / (y[0] - x[0])


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    heights = list(map(int, input().split()))

    visible_buildings = 0

    for i in range(N):
        tmp_visible = 0
        min_inc = 0

        for j in range(i - 1, -1, -1):
            inc = cal_inclination((i, heights[i]), (j, heights[j]))

            if j == i - 1 or inc < min_inc:
                min_inc = inc
                tmp_visible += 1

        max_inc = 0

        for j in range(i + 1, N):
            inc = cal_inclination((i, heights[i]), (j, heights[j]))

            if j == i + 1 or inc > max_inc:
                max_inc = inc
                tmp_visible += 1

        visible_buildings = max(visible_buildings, tmp_visible)

    print(visible_buildings)
