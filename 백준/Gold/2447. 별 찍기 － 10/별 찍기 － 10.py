import sys

intput = sys.stdin.readline

N = int(input())

rs = [[0 for _ in range(N)] for _ in range(N)]


def recursive(sy, ey, sx, ex):
    if sy - ey == 0:
        rs[sy][sx] = 1
        return

    gap = (ey - sy) // 3

    for i in range(sy + gap, sy + gap + gap):
        for j in range(sx + gap, sx + gap + gap):
            rs[i][j] = 0

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            recursive(sy + i * gap, sy + (i + 1) * gap, sx + j * gap, sx + (j + 1) * gap)


recursive(0, N, 0, N)

for r in rs:
    print("".join(["*" if j else " " for j in r]))

