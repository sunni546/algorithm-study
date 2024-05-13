import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    m = int(input())
    s = set()

    for i in range(m):
        cal = input().split()

        if cal[0] == "all":
            s = set(list(range(1, 21)))
        elif cal[0] == "empty":
            s = set()
        else:
            x = int(cal[1])
            if cal[0] == "add":
                s.add(x)
            elif cal[0] == "remove":
                s.discard(x)
            elif cal[0] == "check":
                print(int(x in s))
            elif cal[0] == "toggle":
                if x in s:
                    s.remove(x)
                else:
                    s.add(x)
