import sys
import math

input = sys.stdin.readline


def main(h, w, n):
    x = ((n - 1) % h) + 1
    y = math.ceil(n / h)
    return str(x) + ("0" + str(y))[-2:]


n = int(input())
for _ in range(n):
    print(main(*[int(i) for i in input().split()]))
