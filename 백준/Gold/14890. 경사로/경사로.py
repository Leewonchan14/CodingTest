import sys

input = sys.stdin.readline
from collections import deque


def isValid(arr, l):
    que = deque(arr)
    temp, cnt = que.popleft(), 1
    while que:
        e = que.popleft()
        if temp == e:
            cnt += 1
            continue

        if e < temp:
            if temp - e > 1:
                return False

            que.appendleft(e)

            if len(que) < l:
                return False

            if not all([que[i] == e for i in range(l)]):
                return False

            temp, cnt = que[0], 0
            for _ in range(l):
                que.popleft()

        if e > temp:
            if e - temp > 1:
                return False

            if cnt < l:
                return False

            temp, cnt = e, 1

    return True


def main(maps, l):
    cnt = 0
    for i in range(len(maps)):
        r = maps[i]
        c = [maps[j][i] for j in range(len(maps))]
        if isValid(r, l):
            cnt += 1
        if isValid(c, l):
            cnt += 1
    return cnt


n, l = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]
print(main(maps, l))
