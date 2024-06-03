import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))

    water = 0

    max_height = max(heights)
    height = heights[W - 1]
    end = 0

    for i in range(W - 1, -1, -1):
        if heights[i] == max_height:
            end = i
            break

        if heights[i] > height:
            height = heights[i]

        else:
            water += height - heights[i]

    height = heights[0]

    for i in range(end):
        if heights[i] > height:
            height = heights[i]

        else:
            water += height - heights[i]

    print(water)
