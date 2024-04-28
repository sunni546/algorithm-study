import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, x = map(int, input().split())
    visitors = list(map(int, input().split()))

    if max(visitors) != 0:
        visitor = sum(visitors[:x])
        max_visitor = [visitor, 1]

        for i in range(x, n):
            visitor = visitor - visitors[i - x] + visitors[i]

            if visitor == max_visitor[0]:
                max_visitor[1] += 1
            elif visitor > max_visitor[0]:
                max_visitor = [visitor, 1]

        for m_v in max_visitor:
            print(m_v)
    else:
        print('SAD')
