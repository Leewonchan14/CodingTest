import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
arr = [map(int, input().split()) for _ in range(tc)]

che = [True] * (10 ** 4)
for i in range(2, len(che)):
    if che[i]:
        for j in range(i * 2, len(che), i):
            che[j] = False


def is_prime(i):
    return che[i]


def all_one_change_num(i):
    result = []
    li = list(str(i))
    for i in range(4):
        for j in range(10):
            if i == 0 and j == 0:
                continue
            new_li = li[:]
            new_li[i] = str(j)
            result.append(int("".join(new_li)))

    return result


def bfs(a, b):
    visited = set()
    que = deque()
    que.append((a, 0))
    visited.add(a)

    while que:
        a, cnt = que.popleft()

        if a == b:
            return cnt

        for na in all_one_change_num(a):
            if na not in visited and is_prime(na):
                visited.add(na)
                que.append((na, cnt + 1))

    return "Impossible"


def main(a, b):
    print(bfs(a, b))


for a, b in arr:
    main(a, b)
