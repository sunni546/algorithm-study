import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        W = input().rstrip()
        K = int(input())

        w = len(W)

        W_dict = {}
        min_length = w + 1
        max_length = 0

        for end in range(w):
            if W_dict.get(W[end]):
                W_dict[W[end]].append(end)
            else:
                W_dict[W[end]] = [end]

            k = len(W_dict[W[end]])
            if k >= K:
                start = W_dict[W[end]][k - K]
                length = end - start + 1

                min_length = min(min_length, length)
                max_length = max(max_length, length)

        if 0 < max_length and min_length <= w:
            print(min_length, max_length)

        else:
            print(-1)
