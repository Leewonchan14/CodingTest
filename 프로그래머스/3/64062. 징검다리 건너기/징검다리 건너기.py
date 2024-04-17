def CanBe(mid, stones, length, k):
    mid = mid - 1
    cnt = 0
    for s in stones:
        if s - mid > 0:
            cnt = 0
            continue
        
        cnt += 1
        if cnt >= k:
            return False
        
    return True
    
            
        
    
def solution(stones, k):
    left = 0
    right = max(stones)
    length = len(stones)
    
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if CanBe(mid, stones, length, k):
            result = max(result, mid)
            left = mid + 1
            
        else:
            right = mid - 1
            
    return result
            
    
    
    