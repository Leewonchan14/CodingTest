import math
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.sort()
first = li[0]
pre = 0

_li = []
for i in range(1, len(li)):
    second = li[i]
    gap = second - first
    if pre == 0:
        pre = gap
    pre = math.gcd(pre, gap)
    _li.append(gap)
    first = second
_sum = 0
for gap in _li:
    _sum += gap // pre - 1
    
print(_sum)
    
    