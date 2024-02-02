n = int(input())
li = [True for _ in range(1001)]
li[0] = False
li[1] = False
for i in range(2, 1001):
    if li[i] == True:
        for j in range(i*2,1001,i):
            li[j] = False

li_ = list(map(int, input().split()))
count = 0
for i in li_:
    if li[i]:
        count+=1
print(count)