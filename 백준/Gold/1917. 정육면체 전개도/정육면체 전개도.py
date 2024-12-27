import sys
from collections import deque

input = sys.stdin.readline

maps_li = []
for _ in range(3):
    maps_li.append([[int(i) for i in input().split()] for _ in range(6)])

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def spin(dice, i):

    if i == 0:
        temp = [dice[j] for j in [3, 1, 2, 6]]
        to = [1, 2, 6, 3]

    elif i == 1:
        temp = [dice[j] for j in [5, 1, 4, 6]]
        to = [1, 4, 6, 5]

    elif i == 2:
        temp = [dice[j] for j in [2, 6, 3, 1]]
        to = [1, 2, 6, 3]

    else:
        temp = [dice[j] for j in [4, 6, 5, 1]]
        to = [1, 4, 6, 5]

    for j in range(4):
        dice[to[j]] = temp[j]


def dfs(maps, y, x, dice):
    if dice[1] == True:
        return False

    dice[1] = True

    for i in range(4):
        ny = y + d[i][0]
        nx = x + d[i][1]

        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
            if maps[ny][nx] == 0:
                continue

            maps[ny][nx] = 0
            spin(dice, i)
            if dfs(maps, ny, nx, dice) == False:
                return False
            spin(dice, (i + 2) % 4)


def solve(maps):
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 1:
                maps[r][c] = 0
                dice = [False] * 7
                dfs(maps, r, c, dice)
                if not all([dice[j] for j in range(1, 7)]):
                    return False
                else:
                    return True


def main():
    for maps in maps_li:
        if solve(maps):
            print("yes")
        else:
            print("no")


main()
