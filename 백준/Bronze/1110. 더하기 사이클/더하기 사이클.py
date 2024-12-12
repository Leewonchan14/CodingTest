import sys

input = sys.stdin.readline


def recursion(n, target):
    cnt = 0
    while True:
        cnt += 1
        h10, h1 = divmod(n, 10)
        n = int(f"{h1}{(h10 + h1) % 10}")
        if n == target:
            return cnt


t = int(input())
print(recursion(t, t))
