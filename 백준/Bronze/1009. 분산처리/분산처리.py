import sys

input = sys.stdin.readline

tc = int(input())
li = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [
    5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [0]]

for _ in range(tc):
    a, b = map(int, input().split())
    a %= 10

    if b < len(li[a]):
        print(li[a][b - 1])
    else:
        print(li[a][(b - 1) % len(li[a])])


