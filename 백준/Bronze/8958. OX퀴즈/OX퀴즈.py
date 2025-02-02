import sys
input = sys.stdin.readline

tc= int(input())

for _ in range(tc):
    arr = list(input().strip())
    cnt = 0
    sumv = 0
    for v in arr:
        if v == "O":
            cnt += 1
            sumv += cnt
        else:
            cnt = 0
        
    print(sumv)
            
    