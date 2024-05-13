import sys


def cal_rank(r, s):
    rank = 1

    for i in range(len(r)):
        if score >= r[i]:
            break

        rank += 1

    return rank


if __name__ == '__main__':
    input = sys.stdin.readline
    n, score, p = map(int, input().split())

    if n == 0:
        print(1)
    elif n > 0:
        ranking = list(map(int, input().split()))

        if n == p and ranking[n - 1] >= score:
            print(-1)
        else:
            print(cal_rank(ranking, score))
