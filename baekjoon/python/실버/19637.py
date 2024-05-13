import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())

    combat_powers = []

    for _ in range(n):
        name, max_power = input().rstrip().split()
        combat_powers.append([name, int(max_power)])

    for _ in range(m):
        power = int(input())

        if power <= combat_powers[0][1]:
            print(combat_powers[0][0])
            continue

        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            if power <= combat_powers[mid][1]:
                right = mid

            else:
                left = mid + 1

        print(combat_powers[left][0])
