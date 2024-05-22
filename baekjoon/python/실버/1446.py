import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, D = map(int, input().split())

    shortcut = []
    distance = [0]
    ends = set()

    for _ in range(N):
        start, end, length = map(int, input().split())

        if start >= D or end > D:
            continue

        elif end - start <= length:
            continue

        shortcut.append([start, end, length])
        ends.add(end)

    for i in range(1, D + 1):
        distance.append(distance[i - 1] + 1)
        if i in ends:
            for s in shortcut:
                if s[1] == i:
                    min_length = s[2] + distance[s[0]]
                    distance[i] = min(distance[i], min_length)

    print(distance[D])
