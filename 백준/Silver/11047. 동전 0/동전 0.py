import itertools

n, _sum = map(int, input().split())

li = [int(input()) for _ in range(n)]

ret = 0

for i in range(-1, -len(li) - 1, -1):
    div = _sum // li[i]
    ret += div
    _sum = _sum % li[i]

print(ret)
