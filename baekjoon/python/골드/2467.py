import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    water = list(map(int, input().split()))

    left, right = 0, N - 1

    start, end = left, right
    min_sum = abs(water[left] + water[right])
    tmp_sum = 0

    while start < end:
        if water[start] * water[end] > 0:
            if water[start] > 0:
                tmp_sum = abs(water[start] + water[start + 1])
                if min_sum > tmp_sum:
                    left, right = start, start + 1
            else:
                tmp_sum = abs(water[right - 1] + water[end])
                if min_sum > tmp_sum:
                    left, right = end - 1, end

            break

        tmp_sum = abs(water[start] + water[end])

        if tmp_sum == 0:
            left, right = start, end
            break

        if min_sum > tmp_sum:
            min_sum = tmp_sum
            left, right = start, end

        if abs(water[start + 1] + water[end]) < abs(water[start] + water[end - 1]):
            start += 1
        else:
            end -= 1

    print(water[left], water[right])
