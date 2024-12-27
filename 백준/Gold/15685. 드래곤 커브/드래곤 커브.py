import sys

input = sys.stdin.readline

direcs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def next_dir(direc):
    return direcs[(direcs.index(direc) + 1) % 4]


ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]

n = int(input())
orders = [[int(i) for i in input().split()] for _ in range(n)]
lines = set()


def add_line(x, y, d, g):
    li = [(x, y)]
    x, y = li[-1]
    nx, ny = x + ds[d][0], y + ds[d][1]
    li.append((nx, ny))
    for _ in range(g):
        for j in range(len(li) - 1, 0, -1):
            pre, now = li[j - 1], li[j]
            direc = (pre[0] - now[0], pre[1] - now[1])
            dx, dy = next_dir(direc)
            x, y = li[-1][0] + dx, li[-1][1] + dy
            li.append((x, y))

    for p in li:
        lines.add(p)


def is_square(x, y):
    return all([p in lines for p in [(x, y), (x, y - 1), (x - 1, y), (x - 1, y - 1)]])


def count_square():
    total = 0
    for y in range(1, 101):
        for x in range(1, 101):
            if is_square(x, y):
                total += 1

    return total


def main():
    for x, y, d, g in orders:
        add_line(x, y, d, g)

    return count_square()


print(main())
