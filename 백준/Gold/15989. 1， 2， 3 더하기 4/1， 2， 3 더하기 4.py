import sys

input = sys.stdin.readline


def get_value(n):
    return sum([nn // 2 + 1 for nn in range(n, -1, -3)])


tc = int(input())
for _ in range(tc):
    n = int(input())
    print(get_value(n))
