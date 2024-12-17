def combination(n, k):
    li = []
    result = []

    def recur():
        if len(li) == k:
            result.append(li[:])
            return

        for i in range(n):
            if not li or i > li[-1]:
                li.append(i)
                recur()
                li.pop()

    recur()
    return result


def main(n, arr):
    for li in combination(n, 6):
        print(" ".join([str(arr[i]) for i in li]))


import sys

input = sys.stdin.readline
while True:
    n, *arr = [int(i) for i in input().split()]

    main(n, arr)

    if n == 0:
        break

    print()
