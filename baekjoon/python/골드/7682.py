import sys


def check_game(game, symbol):
    is_valid = False

    for i in range(n):
        # 가로
        if i % 3 == 0:
            is_valid = True

            for j in range(i, i + 3):
                if game[j] != symbol:
                    is_valid = False
                    break

            if is_valid:
                return is_valid

        # 세로
        if i < 3:
            is_valid = True

            for j in range(i, n, 3):
                if game[j] != symbol:
                    is_valid = False
                    break

            if is_valid:
                return is_valid

        # 대각선
        if i == 0 or i == 2:
            is_valid = True

            k = 4
            if i:
                k = 2

            j = i
            for _ in range(3):
                if game[j] != symbol:
                    is_valid = False
                    break

                j += k

            if is_valid:
                return is_valid

    return is_valid


if __name__ == '__main__':
    input = sys.stdin.readline

    n = 9

    while True:
        case = input().rstrip()

        if case == 'end':
            break

        x, o, blank = 0, 0, 0
        for c in case:
            if c == 'X':
                x += 1
            elif c == 'O':
                o += 1
            else:
                blank += 1

        if not blank:
            if x - o == 1:
                if not check_game(case, 'O'):
                    print("valid")
                    continue

        elif x == o:
            if o >= 3:
                if not check_game(case, 'X') and check_game(case, 'O'):
                    print("valid")
                    continue

        elif x == o + 1:
            if x >= 3:
                if not check_game(case, 'O') and check_game(case, 'X'):
                    print("valid")
                    continue

        print("invalid")
