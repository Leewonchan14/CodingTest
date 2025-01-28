import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
maps.append([0] * (m + 1))

for _ in range(n):
    row = [0, *list(map(int, input().split()))]
    maps.append(row)

d = [(-1, 0), (0, -1), (-1, -1)]

for r in range(1, n + 1):
    for c in range(1, m + 1):
        maps[r][c] = max([maps[r + d[i][0]][c + d[i][1]]
                         for i in range(3)]) + maps[r][c]

print(maps[-1][-1])
