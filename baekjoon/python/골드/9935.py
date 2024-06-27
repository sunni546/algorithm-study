import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    text = list(input().rstrip())
    bomb = list(input().rstrip())

    stack = []

    for t in text:
        stack.append(t)

        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

    if stack:
        for s in stack:
            print(s, end='')
    else:
        print('FRULA')
