import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    roads = list(map(int, input().split()))
    oil_prices = list(map(int, input().split()))

    totals = 0
    
    oil_price = oil_prices[0]
    
    for i in range(n - 1):
        if oil_prices[i] < oil_price:
            oil_price = oil_prices[i]

        totals += oil_price * roads[i]

    print(totals)
    