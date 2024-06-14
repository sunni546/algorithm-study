import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    good_number = 0

    for i in range(N):
        a = A[i]

        left, right = 0, N - 1

        while left < right:
            if left == i:
                left += 1
            elif right == i:
                right -= 1

            else:
                if A[left] + A[right] == a:
                    good_number += 1
                    break
                if A[left] + A[right] < a:
                    left += 1
                else:
                    right -= 1

    print(good_number)
