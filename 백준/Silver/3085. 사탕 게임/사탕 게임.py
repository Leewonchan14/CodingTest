import sys

input = sys.stdin.readline


def eat(maps):
    maxv = 0
    for i in range(len(maps)):
        # row
        cnt = 1
        for c in range(1, len(maps)):
            if maps[i][c] != maps[i][c - 1]:
                cnt = 1
            else:
                cnt += 1
                maxv = max(cnt, maxv)
                
        cnt = 1
        for r in range(1, len(maps)):
            if maps[r][i] != maps[r - 1][i]:
                cnt = 1
            else:
                cnt += 1
                maxv = max(cnt, maxv)
    return maxv


def findAll(maps):
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    li = []
    for r in range(len(maps)):
        for c in range(len(maps)):
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                if (
                    0 <= nr < len(maps)
                    and 0 <= nc < len(maps)
                    and maps[nr][nc] != maps[r][c]
                ):
                    li.append((r, c, nr, nc))

    return li


def change(maps, y1, x1, y2, x2):
    maps[y1][x1], maps[y2][x2] = maps[y2][x2], maps[y1][x1]


tc = int(input())

maps = []
for i in range(tc):
    maps.append(list(input().strip()))

findChanges = findAll(maps)

visited = set()
maxv = 0
for c in findChanges:
    y1, x1, y2, x2 = c
    if (y2, x2, y1, x1) in visited:
        continue
    
    visited.add((y2, x2, y1, x1))
    visited.add((y1, x1, y2, x2))
    change(maps, *c)
    maxv = max(eat(maps), maxv)
    change(maps, *c)

print(maxv)
