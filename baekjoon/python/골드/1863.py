import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    skyline = []

    for _ in range(n):
        _, y = map(int, input().split())
        skyline.append(y)

    Y = []
    building = 0

    start_x = 0

    for i in range(n):
        i_y = skyline[i]

        if not i_y:
            start_x = i + 1
            Y = []
            continue

        if i_y not in Y:
            building += 1

        else:
            tmp_Y = Y.copy()
            for _ in range(i, start_x - 1, -1):
                t_y = tmp_Y.pop()

                if t_y == i_y:
                    break

                if t_y < i_y:
                    building += 1
                    break

        Y.append(i_y)

    print(building)
