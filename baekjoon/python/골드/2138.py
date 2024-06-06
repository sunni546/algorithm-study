import sys


def click_switch(light_bulbs, switch):
    for i in [-1, 0, 1]:
        s = switch + i

        if 0 <= s < N:
            light_bulbs[s] = int(not light_bulbs[s])


def get_clicks(light_bulbs, a, click):
    for i in range(0, N - 1):
        if light_bulbs[i] != a[i]:
            click_switch(light_bulbs, i + 1)
            click += 1

    if light_bulbs == a:
        return click
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    before = list(map(int, input().rstrip()))
    after = list(map(int, input().rstrip()))

    min_click = 0

    if before != after:
        not_click_first = before.copy()
        min_click = get_clicks(not_click_first, after, 0)

        if min_click == -1:
            click_switch(before, 0)
            min_click = get_clicks(before, after, 1)

    print(min_click)
