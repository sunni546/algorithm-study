import sys


def cal_rank(s):
    r = {}
    rank = 1

    for i in range(n):
        c = s[i][0]

        if i != 0 and s[i][1] == s[i - 1][1]:
            r[c] = r[s[i - 1][0]]
        else:
            r[c] = rank

        rank += 1

    return r


if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    scores = []

    for i in range(n):
        score = list(map(int, input().split()))
        country = score[0]
        medal = score[1:4]

        scores.append([country, medal])

    scores.sort(key=lambda item: item[1], reverse=True)

    ranks = cal_rank(scores)
    print(ranks[k])
