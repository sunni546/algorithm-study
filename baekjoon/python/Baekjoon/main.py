def cal(x, y):
    return (x + y) // (y + 1)


if __name__ == '__main__':
    h, w, n, m = map(int, input().split())
    print(cal(h, n) * cal(w, m))
