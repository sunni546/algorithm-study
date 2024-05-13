import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    squares = []
    max_height = 0

    for _ in range(N):
        square = list(map(int, input().split()))
        squares.append(square)

        max_height = max(max_height, square[1])

    squares.sort(key=lambda x: x[0])

    area = 0
    width, height = squares[0][0], squares[0][1]
    count_max = 0

    for square in squares:
        if square[1] == max_height:
            count_max += 1

    i = 0
    while i < N:
        if height < squares[i][1] < max_height and count_max:
            area += height * (squares[i][0] - width)

            height = squares[i][1]
            width = squares[i][0]

        elif squares[i][1] == max_height and count_max > 1:
            if height < max_height:
                area += height * (squares[i][0] - width)
                height = squares[i][1]
                width = squares[i][0]

            count_max -= 1

        elif squares[i][1] == max_height and count_max == 1:
            if height < max_height:
                area += height * (squares[i][0] - width) + max_height
            else:
                area += height * (squares[i][0] + 1 - width)

            height = squares[N - 1][1]
            width = squares[N - 1][0]
            break

        i += 1

    for j in range(N - 1, i - 1, -1):
        if squares[j][1] == max_height:
            area += height * (width - squares[j][0])

        elif height < squares[j][1]:
            area += height * (width - squares[j][0])

            height = squares[j][1]
            width = squares[j][0]

    print(area)
