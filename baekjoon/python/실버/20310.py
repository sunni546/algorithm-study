import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    S = list(input().rstrip())

    zero = S.count('0')
    one = S.count('1')

    for _ in range(one // 2):
        S.remove('1')

    S.reverse()

    for _ in range(zero // 2):
        S.remove('0')

    S.reverse()

    for s in S:
        print(s, end='')
