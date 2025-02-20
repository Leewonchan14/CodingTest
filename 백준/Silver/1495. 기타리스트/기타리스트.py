import sys
from collections import deque

input = sys.stdin.readline

n, s, m = map(int, input().split())
arr = [int(i) for i in input().split()]

que = deque([(s, 0)])

hash = {}

maxv = -1

while que:
    p, i = que.popleft()

    if i < len(arr):
        if 0 <= p + arr[i] <= m and (p + arr[i], i + 1) not in hash:
            hash[(p + arr[i], i + 1)] = 0
            que.append((p + arr[i], i + 1))

        if 0 <= p - arr[i] <= m and (p - arr[i], i + 1) not in hash:
            hash[(p - arr[i], i + 1)] = 0
            que.append((p - arr[i], i + 1))

    if i == len(arr) and p > maxv:
        maxv = p

print(maxv)
