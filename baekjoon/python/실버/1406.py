import sys


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


if __name__ == '__main__':
    input = sys.stdin.readline
    text = input().rstrip()
    N = len(text)

    head = Node(None)

    linked_list = head
    for i in range(N):
        linked_list.next = Node(text[i], linked_list)
        linked_list = linked_list.next

    cursor = linked_list

    M = int(input())
    for _ in range(M):
        command = input().rstrip().split()

        if command[0] == 'L':
            if cursor.prev:
                cursor = cursor.prev

        elif command[0] == 'D':
            if cursor.next:
                cursor = cursor.next

        elif command[0] == 'B':
            if cursor.prev:
                cursor.prev.next = cursor.next

                if cursor.next:
                    cursor.next.prev = cursor.prev

                cursor = cursor.prev

        elif command[0] == 'P':
            node = Node(command[1], cursor, cursor.next)

            if cursor.next:
                cursor.next.prev = node

            cursor.next = node

            cursor = cursor.next

    while head:
        if head.value:
            print(head.value, end='')
        head = head.next
