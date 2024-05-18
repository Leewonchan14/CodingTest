import sys
from collections import deque

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

ls = deque()

for i in range(N):
    ls.append(int(input()))

temp = deque()

for i in range(k):
    temp.append(ls.popleft())

new_set = set(temp)
new_set.add(c)

i = 0
maxv = len(new_set)
while i < N + k:
    temp.append(ls.popleft())
    ls.append(temp.popleft())
    new_set = set(temp)
    new_set.add(c)
    maxv = max(maxv, len(new_set))
    i += 1

print(maxv)
