import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    number = input().rstrip()

    n = 0
    i = 0

    while True:
        n += 1
        for num in str(n):
            if num == number[i]:
                i += 1
                if i > len(number) - 1:
                    print(n)
                    exit()
