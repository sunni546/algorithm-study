import sys


def get_step(s):
    step = 0

    for i in range(1, 20):
        for j in range(i):
            if s[j] > s[i]:
                student = s[i]
                s.remove(student)
                s.insert(j, student)

                step += i - j
                break

    return step


if __name__ == '__main__':
    input = sys.stdin.readline
    p = int(input())

    for i in range(p):
        test = list(map(int, input().split()))
        students = test[1:21]

        print(f'{test[0]} {get_step(students)}')
