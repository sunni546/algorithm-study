import sys


def word_to_dic(w):
    d = {}

    for a in w:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    return d


def delete_dic(a, b):
    c = a.copy()

    for key, value in a.items():
        if key in b:
            if value == b[key]:
                c.pop(key)

    return c


def compare_dic(a, b):
    a_k, a_v = '', 0
    for key, value in a.items():
        a_k, a_v = key, value

    if a_k in b:
        if a_v - b[a_k] == 1:
            b.pop(a_k)

            for value in b.values():
                if value == 1:
                    return True

    return False


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    first_word = input().rstrip()

    similar = 0
    first_dic = word_to_dic(first_word)

    for _ in range(n - 1):
        word = input().rstrip()
        dic = word_to_dic(word)

        if dic == first_dic:
            similar += 1
            continue

        new_dic = delete_dic(dic, first_dic)
        new_first_dic = delete_dic(first_dic, dic)

        if len(new_first_dic) <= 1 and len(new_dic) <= 1:
            if not new_dic:
                for value in new_first_dic.values():
                    if value == 1:
                        similar += 1
                        continue

            if not new_first_dic:
                for value in new_dic.values():
                    if value == 1:
                        similar += 1
                        continue

            dic_k, dic_v, first_k, first_v = '', 0, '', 0

            for key, value in new_dic.items():
                dic_k, dic_v = key, value
            for key, value in new_first_dic.items():
                first_k, first_v = key, value

            if dic_k == first_k:
                if abs(dic_v - first_v) == 1:
                    similar += 1
                    continue
            else:
                if dic_v == 1 and first_v == 1:
                    similar += 1
                    continue

        elif len(new_first_dic) == 1 and len(new_dic) == 2:
            if compare_dic(new_first_dic, new_dic):
                similar += 1
                continue

        elif len(new_first_dic) == 2 and len(new_dic) == 1:
            if compare_dic(new_dic, new_first_dic):
                similar += 1
                continue

        elif len(new_first_dic) == 2 and len(new_dic) == 2:
            s = 0

            for key, value in new_dic.items():
                if key not in new_first_dic:
                    s = 2
                    break

                if abs(value - new_first_dic[key]) != 1:
                    s = 2
                    break

                s += value - new_first_dic[key]

            if not s:
                similar += 1
                continue

    print(similar)
