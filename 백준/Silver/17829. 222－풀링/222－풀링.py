import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]


def recursive(y1, y2, x1, x2):
    if y2 - y1 == 2:
        y2 -= 1
        x2 -= 1
        return sorted([inputs[y1][x1], inputs[y1][x2], inputs[y2][x1], inputs[y2][x2]])[-2]

    mid_y = (y1 + y2) // 2
    mid_x = (x1 + x2) // 2
    a = recursive(y1, mid_y, x1, mid_x)
    b = recursive(y1, mid_y, mid_x, x2)
    c = recursive(mid_y, y2, x1, mid_x)
    d = recursive(mid_y, y2, mid_x, x2)

    return sorted([a, b, c, d])[-2]


print(recursive(0, N, 0, N))
