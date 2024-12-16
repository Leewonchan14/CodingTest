import sys, math


input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    N, M, x, y = [int(i) for i in input().split()]
    i = x
    limit = math.lcm(N, M)
    while (((i - 1) % M) + 1) != y:
        i += N
        if i > limit:
            i = -1
            break
    print(i)
