import sys


def check_ball(is_first, color):
    movement = 0
    n = len(color)

    if is_first:
        for k in range(1, n):
            if color[k - 1] + 1 != color[k]:
                movement = n - k
                break
    else:
        for k in range(n - 1, 0, -1):
            if color[k] - 1 != color[k - 1]:
                movement = k
                break

    return movement


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    balls = list(input().rstrip())

    red = []
    blue = []

    for i in range(N):
        if balls[i] == 'R':
            red.append(i)
        else:
            blue.append(i)

    min_movement = N

    if not red or not blue:
        min_movement = 0

    else:
        if balls[0] == 'R':
            min_movement = min(check_ball(True, red), min_movement)
        else:
            min_movement = min(check_ball(True, blue), min_movement)

        if balls[N - 1] == 'R':
            min_movement = min(check_ball(False, red), min_movement)
        else:
            min_movement = min(check_ball(False, blue), min_movement)

        if balls[0] == balls[N - 1]:
            if balls[0] == 'R':
                min_movement = min(len(blue), min_movement)
            else:
                min_movement = min(len(red), min_movement)

    print(min_movement)
