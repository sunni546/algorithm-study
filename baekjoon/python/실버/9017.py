import sys


def cal_score(n, p):
    s = [0 for _ in range(n)]
    score = 1

    for i in range(n):
        if p.count(p[i]) == 6:
            s[i] = score
            score += 1

    return s


def get_team(p):
    ts = [[] for _ in range(max(p))]

    for i in range(len(p)):
        ts[p[i] - 1].append(i)

    return ts


def cal_team_score(s, ts):
    team_scores = [0 for _ in range(len(ts))]

    for i in range(len(ts)):
        if len(ts[i]) == 6:
            for j in range(4):
                team_scores[i] += s[ts[i][j]]

    return team_scores


def get_winner_score(ts):
    ts_tmp = ts.copy()

    while 0 in ts_tmp:
        ts_tmp.remove(0)

    return min(ts_tmp)


def find_winner(p, s):
    teams = get_team(p)
    team_scores = cal_team_score(s, teams)

    winner_score = get_winner_score(team_scores)
    if team_scores.count(winner_score) == 1:
        return team_scores.index(winner_score) + 1
    else:
        winner = team_scores.index(winner_score)
        min_five = teams[winner][4]

        for i in range(len(teams)):
            if i != winner and team_scores[i] == winner_score:
                if min_five > teams[i][4]:
                    winner = i
                    min_five = teams[winner][4]

        return winner + 1


if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())

    for i in range(t):
        n = int(input())
        players = list(map(int, input().split()))

        scores = cal_score(n, players)

        print(find_winner(players, scores))
