import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    max_length = 0
    a_number = {}
    a_index = {}

    j = 0
    for i in range(N):
        if a[i] in a_number:
            if a_number[a[i]] == K:
                max_length = max(max_length, sum(a_number.values()))
                a_number[a[i]] -= 1

                k = a_index[a[i]].pop(0)
                while j < k:
                    a_number[a[j]] -= 1
                    a_index[a[j]].pop(0)
                    j += 1
                j += 1

        if not a[i] in a_index:
            a_index[a[i]] = []
        a_index[a[i]].append(i)

        if not a[i] in a_number:
            a_number[a[i]] = 0
        a_number[a[i]] += 1

    max_length = max(max_length, sum(a_number.values()))
    print(max_length)
