n, _n = map(int, input().split())

li = ["0" for _ in range(n)]

for i in range(_n):
    a,b,c = map(int, input().split())
    for j in range(a - 1, b):
        li[j] = str(c)

print(" ".join(li))