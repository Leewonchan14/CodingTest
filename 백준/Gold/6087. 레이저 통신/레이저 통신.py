import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]

cp = []

for r in range(n):
    for c in range(m):
        if maps[r][c] == "C":
            cp.append((r, c))

cp2, cp1 = cp

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs():
    que = deque()
    coasts = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
    que.append((*cp1, None))
    coasts[cp1[0]][cp1[1]] = [0, 0, 0, 0]
    is_first = True

    while que:
        y, x, pre_dic = que.popleft()

        # if (y, x) == cp2:
        #     return coasts[y][x]

        for i in range(4):
            # 이전과 반대방향은 넘어감
            if (i + 2) % 4 == pre_dic:
                continue

            pre_dic = i if is_first else pre_dic
            is_same_dic = pre_dic == i

            ny, nx = y + dy[i], x + dx[i]
            if inner(ny, nx) and maps[ny][nx] != "*":
                coast = coasts[y][x][pre_dic] + (0 if is_same_dic else 1)
                if coast < coasts[ny][nx][i]:
                    coasts[ny][nx][i] = coast
                    que.append((ny, nx, i))

        is_first = False

    return min(coasts[cp2[0]][cp2[1]])


def main():
    print(bfs())


main()
