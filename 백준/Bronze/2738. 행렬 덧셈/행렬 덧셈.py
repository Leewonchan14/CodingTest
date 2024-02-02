n, _ = map(int, input().split())

li = []

for i in range(n):
    li.append(list(map(int,input().split())))

for i in range(n):
    _li = list(map(int,input().split()))
    for j in range(len(li[0])):
        li[i][j] += _li[j]
    
for i in li:
    i = list(map(str, i))
    print(" ".join(i))
              
