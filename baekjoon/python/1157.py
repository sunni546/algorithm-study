if __name__ == '__main__':
    alphabets = list(input().upper())

    alphabet = []
    number = []

    for a in alphabets:
        if a not in alphabet:
            alphabet.append(a)
            number.append(alphabets.count(a))

    max_num = max(number)
    if number.count(max_num) != 1:
        print('?')
    else:
        print(alphabet[number.index(max_num)])
