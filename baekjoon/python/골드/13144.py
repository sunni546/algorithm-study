import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    numbers = list(map(int, input().split()))

    answer = 0
    unique = [False] * 100000
    start, end = 0, 0

    while start < N and end < N:
        if unique[numbers[end] - 1]:
            for i in range(start, end):
                unique[numbers[i] - 1] = False

                if numbers[i] == numbers[end]:
                    start = i + 1
                    break

        unique[numbers[end] - 1] = True
        end += 1
        answer += end - start

    print(answer)
