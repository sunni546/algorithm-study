import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, d, k, c = map(int, input().split())

    sushi = []
    for _ in range(N):
        sushi.append(int(input()))

    max_types = 0

    for i in range(N):
        eaten_sushi = set()

        for j in range(k):
            sushi_index = i + j
            if sushi_index >= N:
                sushi_index -= N

            eaten_sushi.add(sushi[sushi_index])

        if len(eaten_sushi) == max_types:
            if c not in eaten_sushi:
                max_types += 1
        elif len(eaten_sushi) > max_types:
            max_types = len(eaten_sushi)
            if c not in eaten_sushi:
                max_types += 1

    print(max_types)
