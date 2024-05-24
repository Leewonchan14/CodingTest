def solution(tickets):
    r = []
    ls = ["ICN"]
    
    dic = {}
    visited = {}
    for a,b in tickets:
        visited[(a,b)] = visited.get((a,b), 0) + 1
        
        dic[a] = dic.get(a, [])
        dic[a].append(b)
        
    def recursive(cnt):
        if len(ls) - 1 == len(tickets):
            r.append(ls[:])
            return
        
        if ls[-1] not in dic:
            return
        
        for e in dic[ls[-1]]:
            if visited[(ls[-1], e)] <= 0:
                continue
                
            visited[(ls[-1], e)] -= 1
            ls.append(e)
            recursive(cnt + 1)
            ls.pop()
            visited[(ls[-1], e)] += 1
    
    recursive(0)
    
    r.sort(key=lambda x: "".join(x))
    return r[0] if r else ls
                