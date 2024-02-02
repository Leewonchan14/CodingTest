pre = ""
n = input()
n = int(n)

_count = 0

for i in range(n):
    s = input()
    count = 0
    for j in s :
        if j != pre :
            count +=1
            pre = j
    pre = ""
    if len(set(list(s))) == count:
        _count += 1
print(_count)
