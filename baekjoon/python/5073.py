def is_valid(t):
    if t[0] < t[1] + t[2]:
        return True
    return False


def print_type(t):
    if t[0] == t[1] == t[2]:
        print("Equilateral")
    elif t[0] != t[1] != t[2]:
        print("Scalene")
    else:
        print("Isosceles")


if __name__ == '__main__':
    while True:
        triangle = list(map(int, input().split()))
        triangle.sort(reverse=True)

        if triangle == [0, 0, 0]:
            break
        else:
            if not is_valid(triangle):
                print("Invalid")
            else:
                print_type(triangle)
                