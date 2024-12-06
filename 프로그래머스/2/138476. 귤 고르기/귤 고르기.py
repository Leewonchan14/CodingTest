def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        dic[i] = dic.get(i, 0) + 1
    
    entries = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    rt = 0
    _sum = 0
    
    for size, cnt in entries:
        _sum += cnt
        rt += 1
        if _sum >= k:
            break
    
    return rt