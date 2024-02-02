n, _n = map(int, input().split())

li = [str(i) for i in range(1,n+1)]

for i in range(_n):
    a,b = map(int, input().split())
    li[a-1], li[b-1] = li[b-1], li[a - 1]

print(" ".join(li))