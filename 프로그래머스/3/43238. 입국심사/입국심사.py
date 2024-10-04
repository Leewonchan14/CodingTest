def solution(n, times):
    right = max(times) * n
    left = 0
    
    while left < right:
        mid = (left + right) // 2
        cal = sum([mid // t for t in times])
        
        if cal >= n:
            right = mid
        else:
            left = mid + 1
            
    return left
        