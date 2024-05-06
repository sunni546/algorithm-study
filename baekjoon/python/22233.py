import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())

    memo = set()

    for _ in range(n):
        keyword = input().rstrip()
        memo.add(keyword)

    for _ in range(m):
        keywords = input().rstrip().split(',')

        for k in keywords:
            if k in memo:
                memo.discard(k)

        print(len(memo))
