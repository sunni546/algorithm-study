import sys


def find_heart(c):
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i][j] == '*':
                return [i + 1, j]


def cal_arm(c, h):
    a = [0, 0]

    for j in range(len(c)):
        if c[h[0]][j] == '*':
            if j < h[1]:
                a[0] += 1
            elif j > h[1]:
                a[1] += 1

    return a


def cal_waist(c, h):
    w = 0

    for i in range(h[0] + 1, len(c) - 1):
        if c[i][h[1]] == '*':
            w += 1

    return w


def cal_leg(c, h, w):
    lg = [0, 0]

    for i in range(h[0] + w + 1, len(c)):
        if c[i][h[1] - 1] == '*':
            lg[0] += 1
        if c[i][h[1] + 1] == '*':
            lg[1] += 1

    return lg


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    cookie = []

    for i in range(n):
        cookie.append(list(input().rstrip()))

    heart = find_heart(cookie)
    print(f'{heart[0] + 1} {heart[1] + 1}')

    arm = cal_arm(cookie, heart)
    waist = cal_waist(cookie, heart)
    leg = cal_leg(cookie, heart, waist)
    print(f'{arm[0]} {arm[1]} {waist} {leg[0]} {leg[1]}')
