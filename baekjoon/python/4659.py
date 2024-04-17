def is_gather(c):
    if c in ['a', 'e', 'i', 'o', 'u']:
        return True

    return False


def has_gather(s):
    for ch in s:
        if is_gather(ch):
            return True

    return False


def has_three_consecutive_gather_or_consonant(s):
    if len(s) < 3:
        return False

    for i in range(2, len(s)):
        if is_gather(s[i - 2]) and is_gather(s[i - 1]) and is_gather(s[i]):
            return True
        elif not is_gather(s[i - 2]) and not is_gather(s[i - 1]) and not is_gather(s[i]):
            return True

    return False


def has_same_consecutive(s):
    if len(s) == 1:
        return False

    for i in range(1, len(s)):
        if s[i] == s[i - 1] and s[i] != 'e' and s[i] != 'o':
            return True

    return False


def is_acceptable(p):
    if not has_gather(p):
        return False

    if has_three_consecutive_gather_or_consonant(p):
        return False

    if has_same_consecutive(p):
        return False

    return True


if __name__ == '__main__':
    while True:
        password = input()

        if password == "end":
            break

        if is_acceptable(password):
            print(f'<{password}> is acceptable.')
        else:
            print(f'<{password}> is not acceptable.')
