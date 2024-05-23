import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ls = []


def recursive():
    if len(ls) == M:
        print(" ".join(map(str, ls)))
        return

    for i in range(1, N + 1):
        if ls and ls[-1] >= i:
            continue
        ls.append(i)
        recursive()
        ls.pop()


recursive()
