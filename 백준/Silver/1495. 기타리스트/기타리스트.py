import sys
from collections import deque

input = sys.stdin.readline

n, s, m = map(int, input().split())
arr = [int(i) for i in input().split()]
hash = set()


def bfs(s, i):
    maxv = -1

    def recur(s, i):
        nonlocal maxv
        if s < 0 or s > m or (s, i) in hash:
            return

        hash.add((s, i))

        if i == len(arr):
            maxv = max(maxv, s)
            return

        recur(s + arr[i], i + 1)
        recur(s - arr[i], i + 1)

    recur(s, i)
    return maxv


def main():
    print(bfs(s, 0))


main()
