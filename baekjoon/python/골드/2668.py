import sys


def match_number(n, v, first, second, k):
    if not v[k]:
        first.add(n[k][0])
        second.add(n[k][1])
        v[k] = True

        return match_number(n, v, first, second, n[k][1] - 1)

    if first == second:
        return list(first)
    else:
        return


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    numbers = []
    pick_number = []

    for i in range(N):
        numbers.append((i + 1, int(input())))

    visited = [False] * N

    for i in range(N):
        if not visited[i]:
            tmp_visited = visited.copy()

            pick = match_number(numbers, tmp_visited, set(), set(), i)

            if pick:
                pick_number.extend(pick)
                visited = tmp_visited

    pick_number.sort()

    print(len(pick_number))
    for p in pick_number:
        print(p)
