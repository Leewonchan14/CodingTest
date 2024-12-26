import sys

input = sys.stdin.readline
from collections import deque


def spin_right(ts, t, visited):
    if visited[t]:
        return

    sr = ts[t][2]
    sl = ts[t][6]

    ts[t].appendleft(ts[t].pop())
    visited[t] = True

    # right
    if t + 1 < len(ts) and ts[t + 1][6] != sr:
        spin_left(ts, t + 1, visited)

    # left
    if t - 1 >= 0 and ts[t - 1][2] != sl:
        spin_left(ts, t - 1, visited)


def spin_left(ts, t, visited):
    if visited[t]:
        return

    sr = ts[t][2]
    sl = ts[t][6]

    ts[t].append(ts[t].popleft())
    visited[t] = True

    # right
    if t + 1 < len(ts) and ts[t + 1][6] != sr:
        spin_right(ts, t + 1, visited)

    # left
    if t - 1 >= 0 and ts[t - 1][2] != sl:
        spin_right(ts, t - 1, visited)


def main(ts, spins):
    for t, direc in spins:
        spin = [spin_left, spin_right][(direc + 1) // 2]
        spin(ts, t - 1, [False] * len(ts))

    return len([t for t in ts if t[0] == 1])


t = int(input())

ts = [deque([int(i) for i in list(input().strip())]) for _ in range(t)]
spins = [[int(i) for i in input().split()] for _ in range(int(input()))]
print(main(ts, spins))
