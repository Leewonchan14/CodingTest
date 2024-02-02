n, _n = map(int, input().split())

li = [str(i) for i in range(1,n+1)]

for i in range(_n):
    a,b = map(int, input().split())
    _a = li[:a-1]
    _b = li[a-1:b][::-1]
    _c = li[b:]
    li = sum([_a,_b,_c], [])
print(" ".join(li))
