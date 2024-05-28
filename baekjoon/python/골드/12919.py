import sys


def check_text(s, t):
    if s == t:
        return 1

    if len(s) < len(t):
        if t[-1] == 'A':
            if t[0] == 'B':
                return max(check_text(s, t[:-1]), check_text(s, t[:0:-1]))
            else:
                return check_text(s, t[:-1])
        elif t[0] == 'B':
            return check_text(s, t[:0:-1])

    return 0


if __name__ == '__main__':
    input = sys.stdin.readline
    S = input().rstrip()
    T = input().rstrip()

    print(check_text(S, T))
