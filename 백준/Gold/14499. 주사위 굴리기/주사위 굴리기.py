import sys

input = sys.stdin.readline


def copy(maps, dice, y, x):
    bottom = 1
    top = 3

    print(dice[top])

    if maps[y][x] == 0:
        maps[y][x] = dice[bottom]
    else:
        dice[bottom] = maps[y][x]
        maps[y][x] = 0


def right(c, maps, dice, y, x):
    if x + 1 >= len(maps[0]):
        return y, x

    fro = [dice[i] for i in [1, 5, 3, 4]]
    to = [4, 1, 5, 3]
    for i in range(len(fro)):
        dice[to[i]] = fro[i]

    x += 1
    copy(maps, dice, y, x)

    return y, x


def left(c, maps, dice, y, x):
    if x - 1 < 0:
        return y, x

    fro = [dice[i] for i in [3, 4, 1, 5]]
    to = [4, 1, 5, 3]
    for i in range(len(fro)):
        dice[to[i]] = fro[i]

    x -= 1
    copy(maps, dice, y, x)

    return y, x


def up(c, maps, dice, y, x):
    if y - 1 < 0:
        return y, x

    v = [dice[i] for i in [3, 0, 1, 2]]
    to = [0, 1, 2, 3]
    for i in range(len(v)):
        dice[to[i]] = v[i]

    y -= 1
    copy(maps, dice, y, x)

    return y, x


def down(c, maps, dice, y, x):
    if y + 1 >= len(maps):
        return y, x

    v = [dice[i] for i in [1, 2, 3, 0]]
    to = [0, 1, 2, 3]
    for i in range(len(v)):
        dice[to[i]] = v[i]

    y += 1
    copy(maps, dice, y, x)

    return y, x


def main(maps, calcs, y, x, dice=[0] * 6):
    for c in calcs:
        fun = [right, left, up, down][c - 1]
        y, x = fun(c, maps, dice, y, x)


n, m, y, x, r = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]
calcs = [int(i) for i in input().split()]
main(maps, calcs, y, x)
