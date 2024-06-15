import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))

    min_length = N + 1
    tmp_numbers = deque()
    sum_num = 0

    for number in numbers:
        tmp_numbers.append(number)
        sum_num += number

        while sum_num >= S:
            min_length = min(min_length, len(tmp_numbers))

            sum_num -= tmp_numbers.popleft()

    if min_length > N:
        min_length = 0

    print(min_length)
