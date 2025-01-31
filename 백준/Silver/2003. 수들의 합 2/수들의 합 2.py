import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

sumv = arr[0]
    
l = 0
r = 1
cnt = 0

while True:
    if sumv == m:
        cnt += 1
        sumv -= arr[l]
        l += 1
        continue
        
    if sumv < m:
        if r >= n:
            break
        sumv += arr[r]
        r += 1
        continue
        
    if sumv > m:
        sumv -= arr[l]
        l += 1
        continue
        
print(cnt)

        