import sys


def cal_rank(s, n):
    r = {}

    for i in range(n):
        rank = 0
        for j in range(n):
            if i != j and s[i][1] < s[j][1] and s[i][2] < s[j][2]:
                rank += 1

        r[s[i][0]] = rank + 1

    return r


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    students = []

    for i in range(n):
        x, y = map(int, input().split())
        students.append([i, x, y])

    ranks = cal_rank(students, n)
    for i in range(n):
        print(ranks[i], end=" ")
