import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    cards = deque([i + 1 for i in range(n)])

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())

    print(cards[0])
