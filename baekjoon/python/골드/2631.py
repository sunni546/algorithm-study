import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    students = []
    for _ in range(N):
        students.append(int(input()))

    answer = [1] * N

    for i in range(N):
        for j in range(i):
            if students[i] > students[j]:
                answer[i] = max(answer[j] + 1, answer[i])

    print(N - max(answer))
