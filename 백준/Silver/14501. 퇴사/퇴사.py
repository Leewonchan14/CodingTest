import sys

input = sys.stdin.readline


def recur(arr, li, maxv):
    for i in range(len(arr)):
        hang, money = arr[i]
        if (i + hang - 1) >= len(arr):
            continue

        if li:
            _, end = li[-1]
            if i <= end:
                continue

        li.append((i, i + arr[i][0] - 1))
        maxv = recur(arr, li, maxv)
        li.pop()

    return max(sum([arr[i][1] for i, _ in li]), maxv)


def main(arr):
    maxv = recur(arr, [], 0)
    print(maxv)


n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]
main(arr)
