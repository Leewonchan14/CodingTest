import sys

input = sys.stdin.readline


def isGood(a, boo, b):
    if boo == "<":
        return a < b

    if boo == ">":
        return a > b


def recur(n, arr):
    li = []
    result = []

    def track(k):
        if k == n + 1:
            result.append(li[:])
            return

        for i in range(10):
            if not li or (i not in li and isGood(li[-1], arr[k - 1], i)):
                li.append(i)
                track(k + 1)
                li.pop()

    track(0)
    return result


def main(n, arr):
    result = recur(n, arr)
    a = result[-1]
    b = result[0]

    for li in [a, b]:
        print("".join([str(i) for i in li]))


n = int(input())
arr = input().split()

main(n, arr)
