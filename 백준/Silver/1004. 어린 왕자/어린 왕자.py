import sys
input = sys.stdin.readline

tc = int(input())
n = 0
points = []
x1, y1, x2, y2 = 0, 0, 0, 0


def dist_square(y1, x1, y2, x2):
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2)


def main():
    cnt = 0
    for y, x, r in points:
        a = dist_square(y, x, y1, x1) <= r ** 2
        b = dist_square(y, x, y2, x2) <= r ** 2
        if a ^ b:
            cnt += 1

    return cnt


for _ in range(tc):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    points = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        points.append((y, x, r))

    print(main())
