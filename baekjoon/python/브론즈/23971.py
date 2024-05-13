def cal(x, y):
    return 1 + (x - 1) // (y + 1)
    # (x + y) // (y + 1) 도 가능


if __name__ == '__main__':
    h, w, n, m = map(int, input().split())
    print(cal(h, n) * cal(w, m))
    