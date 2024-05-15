import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    taller = list(map(int, input().split()))
    people = [0 for _ in range(N)]

    for i in range(N):
        height = i + 1
        location = taller[i]

        j = 0
        while j < location + 1:
            if people[j]:
                location += 1
            j += 1

        people[location] = height

    for p in people:
        print(p, end=' ')
