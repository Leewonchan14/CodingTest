def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        dic[i] = dic.get(i, 0) + 1
    
    arr = sorted(dic.items(), key=lambda x : x[1], reverse=True)
    count = 0 
    for i in arr:
        k -= i[1]
        count += 1
        if k <= 0:
            break
        
    return count
        
        
        
        
    
        