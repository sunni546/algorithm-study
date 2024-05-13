import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    x = list(map(int, input().split()))

    x_distances = {x[0], n - x[m - 1]}

    for i in range(1, m):
        x_distances.add((x[i] - x[i - 1] + 1) // 2)

    print(max(x_distances))
