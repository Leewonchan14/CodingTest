def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
        
    for c in completion:
        if c in dic and dic[c] > 1:
            dic[c] -= 1
        elif c in dic and dic[c] == 1:
            del dic[c]
            
    return list(dic.keys())[0]
            
            
    
                
            