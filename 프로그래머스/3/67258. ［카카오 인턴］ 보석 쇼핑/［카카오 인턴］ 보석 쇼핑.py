def solution(gems):
    count = {}
    deq = {}
    for i in gems:
        count[i] = count.get(i, 0) + 1
    
    target = len(count.keys())
    
    left = 0
    right = 0
        
    ls = []
        
    while right < len(gems):
        while right < len(gems) and len(deq.keys()) != target:
            deq[gems[right]] = deq.get(gems[right], 0) + 1
            right += 1
                
        if len(deq.keys()) == target:
            while deq[gems[left]] >= 2:
                deq[gems[left]] -= 1 
                left += 1

            ls.append([left + 1, right])
            
            deq.pop(gems[left])
            left += 1
        
    ls.sort(key=lambda x : (x[1] - x[0], x[0]))
    
    print(ls)
    
    return ls[0]
        
        
    
    
    
    