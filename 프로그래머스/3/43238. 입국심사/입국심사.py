def cal(mid, times):
    return sum([mid // t for t in times])

def solution(n, times):
    left = 0
    right = 10000000000000000000
    # right = 50
    mid = (left + right) // 2
    
    while left != right:
    # for i in range(15):
        r = cal(mid, times)
        if r < n:
            left = mid + 1
        else:
            right = mid
            
        mid = (left + right) // 2
        
        # print(left, mid, right)
        
    return mid
    