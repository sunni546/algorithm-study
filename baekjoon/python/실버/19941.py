import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    location = list(input().rstrip())

    for i in range(n):
        if location[i] == 'P':
            for j in range(i - k, i + k + 1):
                if 0 > j or j > n - 1:
                    continue

                if location[j] == 'H':
                    location[j] = 'E'
                    break

    print(location.count('E'))
