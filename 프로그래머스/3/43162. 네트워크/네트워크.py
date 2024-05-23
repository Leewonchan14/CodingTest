from collections import deque

def solution(n, computers):
    dic = {i:[] for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0:
                continue
            dic[i].append(j)
            dic[j].append(i)
    
    count = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
            
        visited[i] = True
        count += 1
        
        def recursive(s):
            for e in dic[s]:
                if visited[e]:
                    continue
                
                visited[e] = True
                recursive(e)
                
        recursive(i)
        
    return count
            