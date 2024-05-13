import sys


def on_off(s_s):
    return 1 if s_s == 0 else 0


def print_switches(n, s):
    for i in range(n):
        print(s[i], end=' ')
        if (i + 1) % 20 == 0:
            print()


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    switches = list(map(int, input().split()))
    student = int(input())

    for i in range(student):
        gender, k = map(int, input().split())

        if gender == 1:
            for j in range(n):
                if (j + 1) % k == 0:
                    switches[j] = on_off(switches[j])

        elif gender == 2:
            k -= 1
            switches[k] = on_off(switches[k])

            for j in range(1, n // 2 + 1):
                if k - j < 0 or k + j > n - 1:
                    break

                if switches[k - j] != switches[k + j]:
                    break

                switches[k - j] = on_off(switches[k - j])
                switches[k + j] = on_off(switches[k + j])

    print_switches(n, switches)
