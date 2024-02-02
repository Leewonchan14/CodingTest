li = [True for _ in range(100001)]
li[0] = False
li[1] = False

for i in range(2,100001):
    if li[i]:
        for j in range(i*2, 100001, i):
            li[j] = False

a = int(input())
b = int(input())

_li = []

for i in range(a,b+1):
    if li[i]:
        _li.append(i)
        
if len(_li) == 0:
    print(-1)
else :
    print(sum(_li))
    print(min(_li))