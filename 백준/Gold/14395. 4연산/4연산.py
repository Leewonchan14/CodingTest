import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int, input().split())


def plus(x):
    return x * 2


def sub(x):
    return x - x


def mul(x):
    return x ** 2


def div(x):
    if x == 0:
        return x
    return 1


cals = [mul, plus, sub, div]


def to_asci(i):
    return ["*", "+", "-", "/"][i]


def bfs():
    global s, t
    visited = set()
    que = deque([s])
    visited.add(s)

    tree_parents = {}

    if s == t:
        return 0

    # if t % s != 0 and t % 2 != 0 and t != 1:
    #     return -1

    while que:
        s = que.popleft()

        if s == t:
            li = []
            while s in tree_parents:
                s, i = tree_parents[s]
                li.append(i)

            return "".join([to_asci(i) for i in li[::-1]])

        for i in range(4):
            ns = cals[i](s)

            if (i == 0 or i == 1) and ((ns != 0 and t % ns != 0)):
                continue

            if ns not in visited:
                tree_parents[ns] = (s, i)
                visited.add(ns)
                que.append(ns)

    return -1


print(bfs())
