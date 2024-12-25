import sys

input = sys.stdin.readline
n, _n, k = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def spin_k(arr, sy, sx, k):
    y, x = sy, sx
    ey, ex = len(arr) - 1 - sy, len(arr[0]) - 1 - sx

    line = [arr[y][x]]
    for i in range(4):
        while sy <= y + dy[i] <= ey and sx <= x + dx[i] <= ex:
            y = y + dy[i]
            x = x + dx[i]
            line.append(arr[y][x])

    line.pop()
    new_line = line[:]

    for i in range(len(line)):
        new_line[i] = line[(len(line) + i - (k % len(line))) % len(line)]

    y, x = sy, sx

    c = 0
    arr[sy][sx] = new_line[0]
    for i in range(4):
        while sy <= y + dy[i] <= ey and sx <= x + dx[i] <= ex:
            y = y + dy[i]
            x = x + dx[i]
            c += 1
            arr[y][x] = new_line[c % len(new_line)]


def spin(arr, k):
    limit = min(len(arr) // 2, len(arr[0]) // 2)
    for i in range(limit):
        spin_k(arr, i, i, k)


def main(arr, k):
    spin(arr, k)

    for r in arr:
        print(" ".join([str(i) for i in r]))


arr = [[int(i) for i in input().split()] for _ in range(n)]

main(arr, k)
