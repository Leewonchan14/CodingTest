li = [1,1,2,2,2,8]

_li = list(map(int, input().split()))

li = [str(li[i] - _li[i]) for i in range(len(li))]

print(" ".join(li))