import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    roads = list(map(int, input().split()))
    oil_prices = list(map(int, input().split()))
    oil_prices.pop()

    min_price = min(oil_prices)
    min_index = oil_prices.index(min_price)
    
    totals = min_price * sum(roads[min_index:])

    if min_index != 0:
        oil_price = oil_prices[0]

        for i in range(min_index):
            if oil_prices[i] < oil_price:
                oil_price = oil_prices[i]

            totals += oil_price * roads[i]

    print(totals)
