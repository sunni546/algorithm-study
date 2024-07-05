import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    words = []
    for i in range(N):
        words.append(input().rstrip())

    S = ''
    T = ''
    max_similar = 0

    for i in range(N - 1):
        s = words[i]
        for j in range(i + 1, N):
            t = words[j]
            tmp = 0

            if s == t:
                break

            for k in range(min(len(s), len(t))):
                if s[k] != t[k]:
                    break
                tmp += 1

            if tmp > max_similar:
                S = s
                T = t
                max_similar = tmp

    print(S)
    print(T)
