def recursive(k, _sum, n):
    if _sum > n:
        return False
    
    if _sum == n:
        return True
    
    return recursive(k + 1, _sum + k + 1, n)
        
    

def solution(n):
    cnt = 0
    li = []
    for i in range(1, n + 1):
        if recursive(i, i, n):
            li.append(i) 
            cnt += 1
            
    print(li)
    return cnt