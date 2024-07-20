import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    for _ in range(3):
        coins = []
        total = 0

        N = int(input())

        for _ in range(N):
            price, number = map(int, input().split())

            coins.append([price, number])
            total += price * number

        answer = 0

        if total % 2 == 1:
            print(answer)
            continue

        total //= 2
        dp = [True] + [False] * total

        for i in range(N):
            for n in range(total, coins[i][0] - 1, -1):
                if dp[n - coins[i][0]]:
                    for j in range(coins[i][1]):
                        if n + coins[i][0] * j <= total:
                            dp[n + coins[i][0] * j] = True
                        else:
                            break

            if dp[total]:
                answer = 1
                break

        print(answer)
