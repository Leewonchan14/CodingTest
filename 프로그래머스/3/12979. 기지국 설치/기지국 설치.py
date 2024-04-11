import math
def solution(n, stations, w):
    sumv = 0
    ls = []
    for s in stations:
        start = s - w
        end = s + w
        if start < 1:
            start = 1
            
        if end > n :
            end = n
        
        ls.append((start,s,end))
    cnt = 0
    temp = 0
    for start,s,end in ls:
        if start - temp > 1 :
            cnt += math.ceil((start - temp - 1) / (2 * w  + 1))
        temp = end

    if temp < n:
        cnt += math.ceil((n - temp) / (2 * w  + 1))
        
    return cnt
            
    
        
    