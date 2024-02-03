a,b,c = map(int, input().split())
li = [a,b,c]
_max = max(li)
_sum = sum(li)
if _sum - _max <= _max:
    print((_sum - _max) * 2 - 1)
else:
    print(sum(li))