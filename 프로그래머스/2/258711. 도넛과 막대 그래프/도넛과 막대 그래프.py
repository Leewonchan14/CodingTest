["dou", "stick", "pal"]

from collections import deque

def check(start, dic):
    visited = set()
    visited.add(start)
    
    que = deque([])
    que.append(start)
    
    while que:
        p = que.popleft()
        if len(dic.get(p, [])) >= 2:
            return 2
        
        for np in dic.get(p , []):
            if np in visited:
                return 0
            
            visited.add(np)
            que.append(np)
            
    return 1
            
            

def solution(edges):
    dic = {}
    not_key = set()
    result = [0, 0, 0, 0]
    for a, b in edges:
        dic[a] = dic.get(a, [])
        dic[a].append(b)
        not_key.add(b)
        
    k,v = [(k,v) for k,v in dic.items() if len(v) >= 2 and k not in not_key][0]
    result[0] = k
    for n in v:
        result[check(n, dic) + 1] += 1
        
    return result
    
