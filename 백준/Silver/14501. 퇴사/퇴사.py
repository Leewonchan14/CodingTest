import sys

input = sys.stdin.readline


def recur(arr, li, maxv, sumv):
    maxv = max(sumv, maxv)

    for i in range(len(arr)):
        hang, money = arr[i]
        if (i + hang - 1) >= len(arr):
            continue

        if li:
            _, end = li[-1]
            if i <= end:
                continue

        start = i
        end = i + hang - 1

        li.append((start, end))
        maxv = recur(arr, li, maxv, sumv + money)
        li.pop()

    return maxv


def main(arr):
    maxv = recur(arr, [], 0, 0)
    print(maxv)


n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]
main(arr)
