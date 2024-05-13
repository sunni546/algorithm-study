def find_level(num):
    level = 1
    max_num = 1

    while num > max_num:
        max_num += 6 * level
        level += 1

    return level


if __name__ == '__main__':
    n = int(input())
    print(find_level(n))
