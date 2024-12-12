import sys

input = sys.stdin.readline


def recursion(n, target, cnt):
    if cnt != 0 and n == target:
        return cnt

    h10, h1 = divmod(n, 10)
    nn = int(f"{h1}{(h10 + h1) % 10}")
    return recursion(nn, target, cnt + 1)


t = int(input())
print(recursion(t, t, 0))
