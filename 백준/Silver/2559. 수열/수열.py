import sys
input = sys.stdin.readline

N,M = map(int, input().split())

ls = list(map(int, input().split()))

sumv = sum(ls[:M])
maxv = sumv

left = 0
right = M
while right + 1 <= N:
    sumv = sumv + ls[right] - ls[left]
    maxv = max(sumv, maxv)
    left += 1
    right += 1

print(maxv)


