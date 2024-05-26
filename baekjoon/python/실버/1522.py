import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    text = list(input().rstrip())
    n = len(text)

    is_b = []
    for t in text:
        if t == 'b':
            is_b.append(True)
        else:
            is_b.append(False)

    min_change = n

    if True not in is_b or False not in is_b:
        min_change = 0

    else:
        i = 0
        while i < n:
            change_num = 0
            check_b = is_b.copy()

            if i > 0 and check_b[i] and check_b[i - 1]:
                i += 1
                continue

            if check_b[i]:
                if i == n - 1:
                    j = k = 0
                else:
                    j = k = i + 1

                while j != i:
                    if check_b[j]:
                        while check_b[k]:
                            if k == j:
                                break

                            k += 1
                            if k >= n:
                                k -= n

                        if k != j:
                            check_b[k], check_b[j] = check_b[j], check_b[k]
                            if text[k] == 'a':
                                change_num += 1
                        k += 1
                        if k >= n:
                            k -= n

                    j += 1
                    if j >= n:
                        j -= n

                min_change = min(min_change, change_num)

            i += 1

    print(min_change)
