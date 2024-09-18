def solution(want, number, discount):
    want = dict(zip(want, number))
    cnt = 0
    
    for i in range(10):
        if discount[i] in want:
            want[discount[i]] -= 1
            
    if all([v <= 0 for v in want.values()]):
        cnt += 1
    
    for i in range(len(discount) - 10):
        if discount[i] in want:
            want[discount[i]] = want.get(discount[i], 0) + 1
        
        if discount[i + 10] in want:
            want[discount[i + 10]] -= 1
        
        if all([v <= 0 for v in want.values()]):
            cnt += 1
            
    return cnt
        
        
            
        
        
        
            
    
        
        
        
    
    
    

