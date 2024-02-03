_,b = map(int, input().split())
li = list(map(int, input().split()))
__sum = 0
for i in range(len(li) - 2):
    for j in range(i+1 ,len(li) - 1):
        for k in range(j+1 ,len(li)):
            _sum = sum([li[i],li[j],li[k]])
            if _sum > b :
                continue
            if _sum > __sum:
                __sum = _sum
print(__sum)