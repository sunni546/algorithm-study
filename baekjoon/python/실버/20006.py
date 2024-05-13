import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    p, m = map(int, input().split())

    rooms = []

    for _ in range(p):
        l, n = input().rstrip().split()

        i = 0

        while i < len(rooms):
            if len(rooms[i]) == m:
                i += 1
                continue

            if rooms[i][0][0] - 10 <= int(l) <= rooms[i][0][0] + 10:
                rooms[i].append((int(l), n))
                break

            i += 1

        if i == len(rooms):
            rooms.append([(int(l), n)])

    for room in rooms:
        if len(room) == m:
            print("Started!")
        else:
            print("Waiting!")

        room.sort(key=lambda x: x[1])

        for r in room:
            print(r[0], r[1])
