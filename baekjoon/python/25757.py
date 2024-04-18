import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    n, game = input().split()
    players = set()

    for i in range(int(n)):
        name = input().rstrip()
        players.add(name)

    if game == 'Y':
        print(len(players))
    elif game == 'F':
        print(len(players) // 2)
    elif game == 'O':
        print(len(players) // 3)
