import sys


def add_heap(h, k):
    h.append(k)
    k_index = len(h) - 1

    i = (k_index - 1) // 2
    while i > -1:
        if k >= h[i]:
            break

        h[k_index], h[i] = h[i], h[k_index]

        k_index = i
        i = (i - 1) // 2


def delete_heap(h):
    h[0], h[-1] = h[-1], h[0]
    print(h.pop())

    i = 0
    while i < len(h):
        left = (i + 1) * 2 - 1
        right = left + 1

        if left < len(h):
            if right < len(h):
                if h[right] >= h[left] and h[i] > h[left]:
                    h[left], h[i] = h[i], h[left]
                    i = left

                elif h[left] > h[right] and h[i] > h[right]:
                    h[right], h[i] = h[i], h[right]
                    i = right

                else:
                    break

            else:
                if h[i] > h[left]:
                    h[left], h[i] = h[i], h[left]

                break
        else:
            break


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    heap = []

    for _ in range(n):
        x = int(input())

        if x != 0:
            add_heap(heap, x)

        else:
            if not heap:
                print(x)

            else:
                delete_heap(heap)
