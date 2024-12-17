setA = [False] * 21


def calc(li):
    global setA
    if len(li) == 1:
        if li[0] == "all":
            setA = [True] * 21
            return

        if li[0] == "empty":
            setA = [False] * 21
            return

    t, v = li
    v = int(v)

    if t == "add":
        setA[v] = True
        return

    if t == "check":
        if setA[v]:
            print(1)
        else:
            print(0)
        return

    if t == "remove":
        setA[v] = False
        return

    if t == "toggle":
        if setA[v]:
            setA[v] = False
        else:
            setA[v] = True

        return


import sys

input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    calc(input().split())
