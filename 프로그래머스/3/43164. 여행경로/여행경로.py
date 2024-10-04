import heapq

def dfs(visited, start, dic, result, n):
    if len(result) == n + 1:
        return True
    
    for end in sorted(dic.get(start, [])):
        if visited[(start, end)] == 0:
            continue
            
        visited[(start, end)] -= 1
        result.append(end)
        if dfs(visited, end, dic, result, n):
            return True
        result.pop()
        visited[(start, end)] += 1
    

def solution(tickets):
    dic = {}
    visited = {}
    for a, b in tickets:
        dic[a] = dic.get(a, [])
        dic[a].append(b)
        visited[(a, b)] = visited.get((a, b), 0) + 1
        
    result = ["ICN"]
        
    dfs(visited, "ICN", dic, result, len(tickets))
    
    return result
        