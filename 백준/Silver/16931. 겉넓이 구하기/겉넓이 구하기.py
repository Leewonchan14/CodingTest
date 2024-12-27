import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]


def count_line(li):
    total = li[0]
    for i in range(1, len(li)):
        if li[i] > li[i - 1]:
            total += li[i] - li[i - 1]

        if li[i] < li[i - 1]:
            total += li[i - 1] - li[i]

    total += li[-1]
    return total


def main():
    total = n * m * 2
    for cols in maps:
        total += count_line(cols)

    for rows in [[maps[r][c] for r in range(len(maps))] for c in range(len(maps[0]))]:
        total += count_line(rows)

    return total


print(main())
