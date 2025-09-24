import sys

input = sys.stdin.readline

k, n = [int(i) for i in input().split()]

li = [int(input()) for _ in range(k)]

left = 1
right = max(li)
res = -1
while True:
    mid = (left + right) // 2
    cal = sum([i // mid for i in li])
    
    if cal >= n:
        left = mid + 1
        res = mid
    elif cal < n:
        right = mid - 1
        
    if right < left:
        break

print(res)
