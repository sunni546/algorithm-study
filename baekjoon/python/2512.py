import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    budgets = list(map(int, input().split()))
    m = int(input())

    if sum(budgets) > m:
        budgets.sort()

        max_budget = 0

        if budgets[0] * n >= m:
            max_budget = m // n

        else:
            for i in range(n - 1):
                m -= budgets[i]
                max_budget = m // (n - i - 1)

                if max_budget <= budgets[i + 1]:
                    break

        print(max_budget)

    else:
        print(max(budgets))
