import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    vocabulary_book = {}

    for _ in range(n):
        word = input().rstrip()

        if len(word) < m:
            continue

        if word in vocabulary_book:
            vocabulary_book[word] += 1
        else:
            vocabulary_book[word] = 1

    vocabulary_book = sorted(vocabulary_book.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word, _ in vocabulary_book:
        print(word)
