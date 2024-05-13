import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        n, k, t, m = map(int, input().split())

        record = [[]] + [[0 for _ in range(k + 2)] for _ in range(n)]

        for log in range(m):
            i, j, s = map(int, input().split())

            record[i][0] += 1  # 해당 팀의 제출 수
            record[i][j] = max(record[i][j], s)  # 해당 팀의 해당 문제의 최고 점수
            record[i][k + 1] = log  # 해당 팀의 마지막 제출

        rank = 1
        total_score = sum(record[t][1:k + 1])

        for t_number in range(1, n + 1):
            if t == t_number:
                continue

            t_score = sum(record[t_number][1:k + 1])

            if t_score > total_score:
                rank += 1

            elif t_score == total_score:
                if record[t_number][0] < record[t][0]:
                    rank += 1

                elif record[t_number][0] == record[t][0]:
                    if record[t_number][k + 1] < record[t][k + 1]:
                        rank += 1

        print(rank)
